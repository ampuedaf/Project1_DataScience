
# PROYECTO INDIVIDUAL Nº1
## Machine Learning Operations (MLOps)

![]<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/mD6TwLDy/MLOPS2.jpg' border='0' alt='MLOPS2'/></a>
## Indice

------------

- Introducción
- Contenido del repositorio
- Contexto de los datos
- Propuesta de trabajo
- ETL
- EDA
- Machine-learning
- Resultado
- Herramientas utilizadas
- Colaboradores

## Introducción

------------
Este proyecto corresponde al primero de la etapa de* Lab's* del programa de **Data Science de Henry**. El rol a desempeñar es el de **MLOps Engineer.**

<p align="center">
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/xCLWk9md/henry2.png' border='0' alt='henry2'/></a>
</p>

## Contenido del Repositorio.

------------
En este repositorio se encuentran almacenadas dos carpetas y cuatro archivos:
En este repositorio se encuentran almacenadas dos carpetas y cuatro archivos:
- En la carpeta datasets se encuentran siete archivos csv: Estos datasets tienen su origen de un Dataset Padre, del cual proviene de la integración de los 3 datasets otorgados.  Se trabajo de acuerdo a los requerimientos de cada una de las funciones solicitadas.

     - df_funcion1.csv : datos limpios obtenidos después del proceso de ETL, con los datos desanidados, a partir de los cuales se realizó la primera función. denominada : **def developer( desarrollador : str ):**
	 - df_funcion2.csv : datos limpios obtenidos después del proceso de ETL, con los datos desanidados, a partir de los cuales se realizó la segunda función. denominada: **def userdata( User_id : str ):**
	 - df_funcion3.csv : datos limpios obtenidos después del proceso de ETL, con los datos desanidados, a partir de los cuales se realizó la tercera función. Denominada: **def UserForGenre( genero : str ):**
	 - df_funcion4.csv : datos limpios obtenidos después del proceso de ETL, con los datos desanidados, a partir de los cuales se realizó la cuarta función. Denominada: **def best_developer_year( año : int ):**
	 - df_funcion5.csv : datos limpios obtenidos después del proceso de ETL, con los datos desanidados, a partir de los cuales se realizó la quinta función. Denominada: **def developer_reviews_analysis( desarrolladora : str ):**
	 - df_funcion6.csv: datos con solo los campos de interés a partir de los cuales se realizó la última función relacionada a** machine-learning.**


- En la carpeta **src**se encuentran los recursos (imágenes) utilizadas para la elaboración del presente Readme.
- En el archivo **ETL** se encuentra la documentación y el paso a paso del ETL.
- En el archivo **EDA** se encuentra la documentación y el paso a paso del EDA.
- En el archivo **main** se encuentra el programa principal que contiene las siete funciones y su conexión con la API.
- En el archivo **requirements** se encuentran las librerías utilizadas indicadas en la API.

## Contexto de los datos.

Los datos a partir de los cuales se desarrolló el proyecto fueron siete archivos en formato csv: df_funcion1.csv, df_funcion2.csv, df_funcion3.csv, df_funcion4.csv, df_funcion5.csv y df_funcion6.csv.

- Datasets otorgados: [Enlace a los datasets](https://drive.google.com/drive/folders/1qyq-didCwr35Q9m2BOByNjYOf4rSQiYu "dataset")


## Propuesta de trabajo.
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/NFRD7x78/Diagrama-Conceptual-Del-Flujo-De-Procesos.png' border='0' alt='Diagrama-Conceptual-Del-Flujo-De-Procesos'/></a>

## ETL.
- Desanidar datos de diversos campos.
- Revisión, manejo e imputación de nulos.
- Transformaciones de tipo de dato en diversos campos.
- Creación de nuevas columnas con datos relevantes y normalizados.
- Unión de datasets.
- Eliminación de columnas innecesarias.
- Exportación de los datos transformados a un nuevo CSV.

Se puede revisar el paso a paso documentado de este proceso en el siguiente link: Notebook ETL

## EDA.
- Obtención de correlaciones de las variables numéricas.
- Generación de pairplots e histogramas de ciertas variables.
- Detección de patrones.
- Análisis de correlaciones y distribuciones.
- Eliminación de datos con poca influencia o poco útiles.
- Realización de word clouds para descubrir las palabras más frecuentes.
- Elección de las variables para el modelo de Machine Learning.
- Exportación de los datos finales a un nuevo CSV.

Se puede revisar el paso a paso documentado de este proceso en el siguiente link: Notebook EDA

## Machine-learning.

- Filtrar el dataset a partir de los géneros del título ingresado.
- Vectorizar los campos de interés "title" , "tags" y "genres".
- Obtener la similitud de coseno entre el título ingresado y los demás a partir de sus vectores.
- Comparar los índices de similitud y obtener las cinco más similares.
- Crear un diccionario con los datos correspondientes a las cinco titulos de juegos  elegidos.
- Se puede revisar el paso a paso documentado del proceso de ML en la sección final del siguiente link: Notebook ML.

## Resultado.
<a href='https://postimg.cc/PCtnTxX9' target='_blank'><img src='https://i.postimg.cc/wjNq5ySq/image.png' border='0' alt='image'/></a>
El resultado final consiste en una API renderizada con las seis requeridas.

Se puede acceder a ella en el siguiente link:[ API](https://fastapi-5q3t.onrender.com/docs#/default " API")

Se puede revisar el paso a paso documentado de las seis funciones en el siguiente link: Notebook Funciones.

## Herramientas utilizadas.
- Python
- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- FastAPI
- Render API

## Colaboradores.
- Freddy Ampueda.
- correo: ampueda@gmail.com
  
