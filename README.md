# Implementando un modelo de Machine Learning para Clasificar Viajes en Taxi en Nueva York

**Este Laboratorio está inspirado en la unidad 1 del curso [Introduction to Machine Learning in Production (DeepLearning.AI)](https://www.coursera.org/learn/introduction-to-machine-learning-in-production/home/welcome). También se apoya en código para generar el modelo disponible en [este repositorio de Shreya Shankar](https://github.com/shreyashankar/debugging-ml-talk) e implementar un flujo de trabajo usando Github Actions de la [Unidad 4 del curso mencionado anteriormente](https://github.com/jesussantana/DeepLearning.AI-Introduction-to-Machine-Learning-in-Production).**

En este notebook elaboramos un modelo de clasificación de viajes en Taxi en función de la propina recibida por el conductor.
La fuente de datos es obtenida de la NYC Taxi and Limousine Commission (TLC), en particular del año 2020. Los archivos de datos están en el formato 'parquet' y existe un archivo para cada mes (enero a diciembre)


## Descripción
Se define que la propina es 'alta' si es que es superior a un 20% del valor del viaje. La idea es identificar los viajes donde la propina fue 'alta'.

Para lo anterior entrenaremos un modelo de clasificación binaria RandomForest usando los datos de los viajes de enero de 2020; luego probarenos el modelo con los restantes datos (febrero a diciembre), y compararemos el performance con métricas como el F1 Score, Accuracy y otros.

## Estructura
T1_productos_datos/
├── references/
│ └── pruebas_estadisticas.md
│ └── data_dictionary_trip_records_yellow.pdf
├── model/
│ └── random_forest.joblib
├── notebooks/
│ └── .Taxi_main.ipynb
├── src/
│ ├── init.py
│ ├── baja_datos_taxi.py
│ ├── preprocesamiento.py
└── README.md
└── requirements.txt


## Uso

1. Descarga el repositorio
2. Ejecuta el notebook

## Nota:
* Los datos no se encuentran en el repositorio. El código los descarga cada vez que se éste se ejecuta. 


