# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:48:58 2023

@author: jumaf
"""

import os
import pandas as pd
from utils.config import DIRECTORIO
from utils.constants import (
    COLUMNAS_COMUNES, 
    COLUMNA_A_CAMBIAR, 
    NUEVO_NOMBRE_COLUMNA, 
    COLUMNAS_NO_REEMPLAZAN_VALOR,
    PREGUNTAS_PARA_AGRUPAR,
)
from utils.functions import (
    cargar_archivo,
    filtrar_columnas,
    reemplazar_respuestas,
    agrupar_preguntas,
    consolidar_otras_preguntas,
    ordenar_columnas,
    renombrar_columnas_con_diccionario
)

def main():
    dataframes = []
    
    print('Inicia la lectura de archivos xlsx con las encuestas de cada año:')
    
    for filename in os.listdir(DIRECTORIO):
        if filename.endswith(".xlsx"):
            cohorte = int(os.path.splitext(filename)[0])
            df = cargar_archivo(cohorte, filename, DIRECTORIO, COLUMNA_A_CAMBIAR, NUEVO_NOMBRE_COLUMNA)
            dataframes.append(df)

    print('\nSe concatenan las encuestas...')
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Además, se pasa el dni a Int64, no float
    combined_df["documento"] = pd.to_numeric(combined_df["documento"], errors='coerce').astype('Int64')
    
    combined_df = filtrar_columnas(combined_df, COLUMNAS_COMUNES)
    combined_df = reemplazar_respuestas(combined_df, COLUMNAS_NO_REEMPLAZAN_VALOR)

    print('Se agrupan los resultados...')
    df_consolidado = agrupar_preguntas(combined_df, PREGUNTAS_PARA_AGRUPAR)
    df_consolidado = consolidar_otras_preguntas(combined_df, df_consolidado, PREGUNTAS_PARA_AGRUPAR)

    print('Se definen los nombres reales para las preguntas...')
    df_consolidado = renombrar_columnas_con_diccionario(df_consolidado, PREGUNTAS_PARA_AGRUPAR)

    print('Se ordenan las columnas...')
    df_consolidado = ordenar_columnas(df_consolidado)
    
    return df_consolidado

if __name__ == "__main__":

    consolidated_df = main()

    print('Se exportan a encuestas-procesadas.xlsx los datos procesados para todos los años...')
    consolidated_df.to_excel('encuestas-procesadas.xlsx')

    print('Procesamiento finalizado.')
