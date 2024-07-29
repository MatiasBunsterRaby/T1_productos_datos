import pandas as pd

# URL base para los archivos parquet
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-"

tope_registros = 100000
def load_monthly_data():
    """
    Lee los archivos parquet desde la URL y devuelve un DataFrame por cada mes.
    
    Returns:
    dict: Un diccionario con los DataFrames para cada mes, con claves 'taxi_data_MM'.
    """
    taxi_dataframes = {}
    
    # Itera sobre los meses del 01 al 12
    for month in range(1, 13):
        month_str = f"{month:02d}"
        file_url = f"{base_url}{month_str}.parquet"
        
        # Leer el archivo y cargarlo en un DataFrame
        try:
            df = pd.read_parquet(file_url, engine='pyarrow')
            print(f"Archivo {file_url} cargado en DataFrame correctamente.")
            
            df = df.sample(tope_registros)
            
            # Almacenar el DataFrame en el diccionario con una clave específica para el mes
            taxi_dataframes[f"taxi_data_{month_str}"] = df
        
        except Exception as e:
            print(f"Error al cargar el archivo {file_url} en DataFrame: {e}")
    
    return taxi_dataframes

