# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 20:49:36 2023

@author: jumaf
"""
import os
import re
import pandas as pd
import numpy as np

def cargar_archivo(cohorte, filename, DIR, columna_a_cambiar, nuevo_nombre_columna):
    file_path = os.path.join(DIR, filename)
    print(f'Leyendo archivo XLSX: {filename}')

    df = pd.read_excel(file_path, header=0)

    df.columns = df.columns.str.lower().str.replace(' ', '_')
    df['cohorte'] = cohorte

    if columna_a_cambiar in df:
        df = df.rename(columns={columna_a_cambiar: nuevo_nombre_columna})

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

def filtrar_columnas(df, columnas_comunes):
    return df[columnas_comunes]

def reemplazar_respuestas(df, columnas_no_reemplazan_valor):
    for col in df.columns:
        if col not in columnas_no_reemplazan_valor:
            df[col] = df[col].apply(lambda x: col if x == 1 else np.nan)
    return df

def agrupar_preguntas(df, preguntas_para_agrupar):
    df_consolidado = pd.DataFrame()
    for pregunta in preguntas_para_agrupar.keys():
        columnas_a_agrupar = [col for col in df.drop(['documento', 'cr', 'carrera', 'cohorte'], axis=1) if pregunta == int(col.split('-')[0])]
        df_consolidado[f'{pregunta}'] = df.apply(obtener_valor_no_nulo, args=(columnas_a_agrupar,), axis=1)
    return df_consolidado

def consolidar_otras_preguntas(df, df_consolidado, preguntas_para_agrupar):
    for columna in df.columns:
        if columna.split('-')[0].isdigit():
            numero_pregunta = int(columna.split('-')[0])
            if numero_pregunta not in preguntas_para_agrupar:
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

def renombrar_columnas_con_diccionario(df, questions_dict):
    for number, question in questions_dict.items():
        str_number = str(number)
        if str_number in df.columns:
            df = df.rename(columns={str_number: question})
    return df
