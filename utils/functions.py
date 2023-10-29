# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:49:36 2023

@author: jumaf
"""
import os
import re
import pandas as pd
import numpy as np
from utils.constants import (
    COLUMNAS_COMUNES, 
    COLUMNA_A_CAMBIAR, 
    NUEVO_NOMBRE_COLUMNA, 
    COLUMNAS_NO_REEMPLAZAN_VALOR,
    PREGUNTAS_PARA_AGRUPAR,
)

from utils.config import DIRECTORIO

def cargar_archivo(cohorte, filename):
    file_path = os.path.join(DIRECTORIO, filename)
    print(f'Leyendo archivo XLSX: {filename}')

    df = pd.read_excel(file_path, header=0)

    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['cohorte'] = cohorte

    if COLUMNA_A_CAMBIAR in df:
        df = df.rename(columns={COLUMNA_A_CAMBIAR: NUEVO_NOMBRE_COLUMNA})

    if cohorte < 2017:
        df = df.rename(columns=rename_columns)
        df['6-medio_o_forma_por_el_cual_conoció_la_universidad'] = np.nan

    return df

# Función para renombrar las columnas
def rename_columns(col_name):
    parts = col_name.split("-", 1)
    if len(parts) == 2:
        num, desc = parts
        num = int(num)
        if num >= 6:
            new_col_name = f"{num + 1}-{desc}"
            return new_col_name
    return col_name


# Función para obtener el valor no nulo de las columnas especificadas
def obtener_valor_no_nulo(row, columnas):
    for col in columnas:
        if not pd.isna(row[col]):
            return row[col]
    return np.nan

def filtrar_columnas(df):
    return df[COLUMNAS_COMUNES]

def reemplazar_respuestas(df):
    for col in df.columns:
        if col not in COLUMNAS_NO_REEMPLAZAN_VALOR:
            df[col] = df[col].apply(lambda x: col if x == 1 else np.nan)
    return df

def agrupar_preguntas(df):
    df_consolidado = pd.DataFrame()
    for pregunta in PREGUNTAS_PARA_AGRUPAR.keys():
        columnas_a_agrupar = [col for col in df.drop(['documento', 'cr', 'carrera', 'cohorte'], axis=1) if pregunta == int(col.split('-')[0])]
        df_consolidado[f'{pregunta}'] = df.apply(obtener_valor_no_nulo, args=(columnas_a_agrupar,), axis=1)
    return df_consolidado

def consolidar_otras_preguntas(df, df_consolidado):
    for columna in df.columns:
        if columna.split('-')[0].isdigit():
            numero_pregunta = int(columna.split('-')[0])
            if numero_pregunta not in PREGUNTAS_PARA_AGRUPAR:
                df_consolidado[f'{columna}'] = df[columna]
        else:
            df_consolidado[columna] = df[columna]
    return df_consolidado

def sort_columns(column_name):
    match = re.search(r'\d+', column_name)
    if match:
        return (int(match.group()), column_name)
    else:
        return (-1, column_name)  # Un número negativo para que queden al principio

def ordenar_columnas(df):
    sorted_columns = sorted(df.columns, key=sort_columns)
    return df.reindex(columns=sorted_columns)