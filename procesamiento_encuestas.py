# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:48:58 2023

@author: jumaf
"""

import os
import pandas as pd
from utils.config import DIRECTORIO
from utils.functions import (
    cargar_archivo,
    filtrar_columnas,
    reemplazar_respuestas,
    agrupar_preguntas,
    consolidar_otras_preguntas,
    ordenar_columnas
)

def main():
    dataframes = []
    
    print('Inicia la lectura de archivos xlsx con las encuestas de cada año:')
    
    for filename in os.listdir(DIRECTORIO):
        if filename.endswith(".xlsx"):
            cohorte = int(os.path.splitext(filename)[0])
            df = cargar_archivo(cohorte, filename)
            dataframes.append(df)

    print('Se concatenan las encuestas...')
    combined_df = pd.concat(dataframes, ignore_index=True)

    combined_df = filtrar_columnas(combined_df)
    combined_df = reemplazar_respuestas(combined_df)

    print('Se agrupan los resultados...')
    df_consolidado = agrupar_preguntas(combined_df)
    df_consolidado = consolidar_otras_preguntas(combined_df, df_consolidado)

    print('Se ordenan las columnas...')
    df_consolidado = ordenar_columnas(df_consolidado)

    print('Procesamiento finalizado')
    
    return df_consolidado

if __name__ == "__main__":
    consolidated_df = main()
    consolidated_df.to_excel('encuestas-procesadas.xlsx')
