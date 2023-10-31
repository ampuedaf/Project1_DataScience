from fastapi import FastAPI
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = FastAPI()

#aca cargo todos los dataframe que vamos a utilizar
df_1_2 = pd.read_csv(r"datasets/df_funcion1.csv")
df_1_3 = pd.read_csv(r"datasets/df_funcion2.csv")
df_1_4 = pd.read_csv(r"datasets/df_funcion3.csv")
df_1_5 = pd.read_csv(r"datasets/df_funcion4.csv")
df_1_6 = pd.read_csv(r"datasets/df_funcion5.csv")
df_1_7 = pd.read_csv(r"datasets/df_funcion6.csv")


# Endpoints 1



@app.get('/developer/{desarrollador}')
def developer( desarrollador ):
    """
    Esta función al poner como parametro un desarrollador dará como resultado la cantidad de items y porcentaje  de contenido FREE 
    por año segun empresa desarrolladora
    """
     # Verifica que desarrollador sea un string
    if not isinstance(desarrollador, str):
        return {"Error": f"'{desarrollador}' is not a string"}
   
    # Normaliza desarrollador esto con el fin si escribe mayuscula o  minuscula noy hay problema
    desarrollador = desarrollador.strip().title()
    
    #filtramos en la columna price todo lo que contenga la palabra Free
    df_price= df_1_2[df_1_2['price'].str.contains('Free')]  
    
    #Pasamos por parametro el valor de la empresa desarrolladora 
    df_Filtrado = df_price[df_price['developer']== desarrollador]
    
    # Agrupamos las fechas con la empresa desarrolladora
    df_grouped = df_Filtrado.groupby(['developer', 'release_date']).size().reset_index(name='cantidad_item')
   
    #Sacamos el total de Items
    total_count = df_grouped['cantidad_item'].sum()
    
    #Creamos una nueva columna para obtener el porcentaje 
    df_grouped['contenido_Free'] = (df_grouped['cantidad_item'] / total_count) * 100
    resultados = df_grouped[['release_date', 'cantidad_item', 'contenido_Free']].head().to_dict(orient='records')
    return resultados
    
# Endpoints 2


@app.get('/userdata/{User_id}')
def userdata( User_id : str ):
    """
    Esta función al poner como parametro un user_id , devolvera la cantidad de dinero gastado 
    por el usuario, el porcentaje de recomendaciónen base a review recommend y la cantidad de
    items
    """
    # Verifica que User_id  sea un string
    if not isinstance(User_id, str):
        return {"Error": f"'{User_id}' is not a string"}
    
    # Normaliza User_id 
    User_id = User_id.strip().title()

    #Filtramos   la columna user_id  que pasamos por parametro
    user_frame = df_1_3[df_1_3['user_id'] == User_id]
    suma_price = round(user_frame['price'].sum(),2)
    
    # Calculamos el porcentaje con la columna recommend
    recommendation_percentage = round((user_frame['recommend'].sum() / len(user_frame)) * 100,2)
    item_count = len(user_frame)
    resultado = {"Usiario":User_id,"Dinero gastado":suma_price," % de recomendación":recommendation_percentage,"cantidad de items":item_count}
    return resultado 

## Endpoints 3

@app.get('/UserForGenre/{genero}')
def UserForGenre( genero : str ):
    """
    Esta funcióndevuelve el usuario que acumula mas horas jugadas para el genero dado, y una 
    lista de acumulación de horas jugadas por año de lanzamiento.
    """

    # Verifica que genero sea un string
    if not isinstance(genero, str):
        return {"Error": f"'{genero}' is not a string"}
   
    # Normaliza genero esto con el fin si escribe mayuscula o  minuscula noy hay problema
    genero = genero.strip().title()
    
    
    #Filtro primero el genero  que piden:
    f_generoAccion = df_1_4[df_1_4['genres'] == genero]
    
    # aca vamos agrupar los datos por user_id y sumamos  la columna suma_playtime_forever para luego buscar el usuario que mas sume
    usuario_mas_horas = f_generoAccion.groupby('user_id')['suma_playtime_forever'].sum().idxmax()
   
    #ahora hacemos un dataframe con el usuario  obtenido en el paso anterior.
    df_usuario_max_horas=f_generoAccion[f_generoAccion['user_id']==usuario_mas_horas]
    
    # En este ultimo paso vamos agrupar la suma total se horas jugadas por cada una de las fechas.
    df_agrupado_anio = df_usuario_max_horas.groupby('release_date')['suma_playtime_forever'].sum()
    diccionario = df_agrupado_anio.to_dict()
    resultado2 = {"Usuario con más horas jugadas para Género ":genero}
    return resultado2,usuario_mas_horas,diccionario

# Endpoints 4

@app.get('/developer_year/{anio}')
def developer_year(anio: int):
    """
    Esta función al poner un año determinado, devolverá  el top 3 de desarrolladores con juegos mas recomendados.
    """
    df_4 = pd.read_csv(r"datasets/df_funcion4.csv")
    df_filtrado = df_4[df_4['posted'] == anio]
    df_filtrado = df_filtrado[df_filtrado['recommend'] == True]
    desarrolladores = df_filtrado['app_name'].value_counts().reset_index()
    desarrolladores.columns = ['app_name', 'count']
    desarrolladores = desarrolladores.sort_values(by='count', ascending=False)
    top_desarrolladores = desarrolladores.head(3)
    dict_desarrolladores = top_desarrolladores.to_dict(orient='records')
    lista_puestos = [{"Puesto " + str(i+1): dict_desarrolladores} for i, dict_desarrolladores in enumerate(dict_desarrolladores)]
    return lista_puestos

# Endpoints 5

@app.get('/developer2/{desarrolladora}')
def developer2( desarrolladora : str ):
    """
    Esta funcion al poner una empresa desarrolladora, devolverá un diccionario con el nombre del desarrollador como
    llave y una lista con la cantidad total de registros de de reseñas de usuarios que se encuentran categorizados
    por un analisis de sentimiento.
    """

    # Verifica que desarrollador sea un string
    if not isinstance(desarrolladora, str):
        return {"Error": f"'{desarrolladora}' is not a string"}
   
    # Normaliza desarrolladora 
    desarrolladora = desarrolladora.strip().title() 
    
    # Filtrar las filas del DataFrame para  el developer dado
    df_filtered = df_1_6[df_1_6['developer'] == desarrolladora]
    
    # Cuenta la cantidad de registros para cada categoría de sentimiento
    sentiment_counts = df_filtered['sentiment-analysis'].value_counts()
    
    # Convierte el resultado en un diccionario
    result = {
    desarrolladora:{   
    'Negative': int(sentiment_counts.get(0, 0)),
    'Positive': int(sentiment_counts.get(2, 0))}
    }
    return result

# Modelo de Machine LEarning:

# Crear un vectorizador TF-IDF para convertir títulos en vectores numéricos
# Crear una matriz TF-IDF para representar los juegos
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(df_1_7.head()['title'] + ' ' + df_1_7.head()['tags'] + ' ' + df_1_7.head()['genres'])

# Calcular la similitud de coseno entre los juegos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Endpoints 6


# Función definida para el sistema de recomendación item-item:
@app.get('/recomendacion_juego/{title}')
def recomendacion_juego(title, num_recommendations=5):
    """
    Esta función  devuelve 5 juegos recomendados. Esta función se hizo con la similitud del coseno entre los juegos.
    Para esta función se  tuvo que crear un vectorizador TF_IDF y una matriz TF-IDF.
    """
    idx = df_1_7[df_1_7['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    num_recommendations = int(num_recommendations)
    sim_scores = sim_scores[1:num_recommendations+1]  
    game_indices = [i[0] for i in sim_scores]
    resultado3 = {"Juegos recomendados  por  Item-Item ":title}
    diccionario2 = df_1_7['title'].iloc[game_indices].tolist()
    return resultado3,diccionario2
    


    
