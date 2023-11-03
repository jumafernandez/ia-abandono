import pandas as pd
import os

def load_and_rename_file(file_path, year):
    # Carga el archivo XLSX en un DataFrame
    df = pd.read_excel(file_path)
    
    # Renombra las columnas basándote en su posición
    df.columns = [col if col != df.columns[6] else f"1-{year}" for col in df.columns]
    df.columns = [col if col != df.columns[7] else f"2-{year}" for col in df.columns]
    
    return df

# Define una función para seleccionar las columnas relevantes
def seleccionar_columnas(row):
    # Año de ingreso del estudiante
    anio_ingreso = row['anio_ingreso']
    
    # Generar nombres de columnas a seleccionar
    columnas_seleccionadas = ['legajo', 'numero_documento', 'anio_ingreso', 'sede_sca', 'carrera', 'plan_estudios']
    columnas_seleccionadas.extend([f'{i}-{anio_ingreso}' for i in range(1, 3)])
    columnas_siguientes = [f'{i}-{anio_ingreso + 1}' for i in range(1, 3)]
    
    # Unir las listas de columnas
    columnas_seleccionadas.extend(columnas_siguientes)
    
    # Seleccionar solo las columnas relevantes
    return row[columnas_seleccionadas]


if __name__ == '__main__':
    
    FOLDER_PATH = 'C:/Users/jumaf/Documents/GitHub/ia-abandono/activos-por-anio'

    COHORTE_DESDE = 2013
    COHORTE_HASTA = 2022
    
    consolidated_data = None

    # Se le suma 2 a COHORTE_HASTA dado que range hace hasta -1 y además necesito verificar
    # la actividad del año anterior
    for year in range(COHORTE_DESDE, COHORTE_HASTA+2):

        file_name = f"{year}.xlsx"
        file_path = os.path.join(FOLDER_PATH, file_name)

        if os.path.exists(file_path):
            print(f'Se carga el archivo {file_name}')
            df = load_and_rename_file(file_path, year)
            
            #df = df[df['anio_ingreso'] >= ANIO_DESDE & df['anio_ingreso'] >= ANIO_HASTA]             

            if consolidated_data is None:
                consolidated_data = df
            else:               
                consolidated_data = pd.concat([consolidated_data, df], ignore_index=True, sort=False)
                # Agrupar por 'legajo' y agregar los valores
                consolidated_data = consolidated_data.groupby('legajo').first().reset_index()

    print(f'Se filtran los estudiantes desde {COHORTE_DESDE} únicamente.')
    # Filtra las filas con anio_ingreso >= 2013
    df_filtrado = consolidated_data[(consolidated_data['anio_ingreso'] >= 2013) & (consolidated_data['anio_ingreso'] <= 2022)]
    
    df_filtrado = df_filtrado.copy()

    print('Nos quedamos con la actividad de los primeros 2 años únicamente.')
    df_filtrado.loc[:, 'activo-1c'] = df_filtrado.apply(lambda row: row[f"1-{row['anio_ingreso']}"], axis=1)
    df_filtrado.loc[:, 'activo-2c'] = df_filtrado.apply(lambda row: row[f"2-{row['anio_ingreso']}"], axis=1)
    df_filtrado.loc[:, 'activo-3c'] = df_filtrado.apply(lambda row: row[f"1-{row['anio_ingreso'] + 1}"], axis=1)
    df_filtrado.loc[:, 'activo-4c'] = df_filtrado.apply(lambda row: row[f"2-{row['anio_ingreso'] + 1}"], axis=1)    

    columnas = ['legajo', 'numero_documento', 'anio_ingreso', 'sede_sca', 'carrera', 'plan_estudios', 'activo-1c', 'activo-2c', 'activo-3c', 'activo-4c']
    print('Nos quedamos con las columnas y representación de las mismas que nos interesan: {columnas}')
    df_final = df_filtrado[columnas].fillna(0)

    print(f'Se exportan a results/activos-procesados-{COHORTE_DESDE}-{COHORTE_HASTA}.xlsx para los datos procesados.')
    df_final.to_excel(f'results/activos-procesados-{COHORTE_DESDE}-{COHORTE_HASTA}.xlsx', index=False)

    print('Procesamiento finalizado.')
