# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 07:27:22 2023

@author: jumaf
"""

import pandas as pd

# Cargo el dataframe y borro las filas con NaN en 'documento'
print('Se cargan los datos de las encuestas y se modifican los tipos de datos.')
df_encuestas = pd.read_excel('results/encuestas-procesadas.xlsx')
df_encuestas = df_encuestas.dropna(subset=['documento'])

df_encuestas['documento'] = pd.to_numeric(df_encuestas['documento'], errors='coerce').astype('Int64')
df_encuestas['1-¿Con quien vas a vivir durante el periodo de clases?'] = df_encuestas['1-¿Con quien vas a vivir durante el periodo de clases?'].astype("category")
df_encuestas['2-¿Por qué medio te trasladarás hasta la sede donde va a cursar durante el periodo de clases?'] = df_encuestas['2-¿Por qué medio te trasladarás hasta la sede donde va a cursar durante el periodo de clases?'].astype("category")
df_encuestas['6-medio_o_forma_por_el_cual_conoció_la_universidad'] = df_encuestas['6-medio_o_forma_por_el_cual_conoció_la_universidad'].astype("category")
df_encuestas['11-¿El Colegio es…'] = df_encuestas['11-¿El Colegio es…'].astype("category")
df_encuestas['12-número_del_colegio'] = df_encuestas['12-número_del_colegio'].astype("category")
df_encuestas['13-nombre_del_colegio'] = df_encuestas['13-nombre_del_colegio'].astype("category")
df_encuestas['14-partido/depto'] = df_encuestas['14-partido/depto'].astype("category")
df_encuestas['14-país'] = df_encuestas['14-país'].astype("category")
df_encuestas['14-provincia'] = df_encuestas['14-provincia'].astype("category")
df_encuestas['15-El Título que tenés o vas a tener es (Opciones)'] = df_encuestas['15-El Título que tenés o vas a tener es (Opciones)'].astype("category")
df_encuestas['16-Orientación del título de Nivel Medio o Polimodal'] = df_encuestas['16-Orientación del título de Nivel Medio o Polimodal'].astype("category")
df_encuestas['22-¿En cuál de las siguientes ramas de la actividad ubicarías a tu trabajo principal?'] = df_encuestas['22-¿En cuál de las siguientes ramas de la actividad ubicarías a tu trabajo principal?'].astype("category")
df_encuestas['30-otros_(especificar)'] = df_encuestas['30-otros_(especificar)'].astype("category")
df_encuestas['33-son_jubilados_o_pensionados'] = df_encuestas['33-son_jubilados_o_pensionados'].astype("category")
df_encuestas['34-padre'] = df_encuestas['34-padre'].astype("category")
df_encuestas['37-especificar'] = df_encuestas['37-especificar'].astype("category")

print('Se cargan los datos relativos a la actividad.')
df_actividad = pd.read_excel('results/activos-procesados-2013-2022.xlsx')

print('Se integran los datos y se eliminan los nulos.')
# Unir los DataFrames por 'documento' y 'documento' y elimino los que tienen 'documento' como NaN
df = df_actividad.merge(df_encuestas, left_on='numero_documento', right_on='documento', how='left')
df = df.dropna(subset=['documento'])

print('Se renombran las columnas y se eliminan las que no son necesarias.')
# Reemplazo 0 por False y 1 por True en las columnas de actividad
columnas_a_reemplazar = ['activo-1c', 'activo-2c', 'activo-3c']
df[columnas_a_reemplazar] = df[columnas_a_reemplazar].replace({0: False, 1: True})

# Se considera que abandonan quienes no se inscriben al 3er cuatrimestre
df['abandono'] = ~df['activo-3c']

# Elimino las columnas que no me sirven
columnas_a_eliminar = ['legajo', 'carrera_y', 'cohorte', 'documento', 'sede', 'activo-3c', 'activo-4c']
df = df.drop(columnas_a_eliminar, axis=1)

# Renombrar las columnas en función de las necesidades y elimino las que no me sirven
df = df.rename(columns={'carrera_x': 'carrera', 'sede_sca': 'sede'})

# Se listas las columnas en el orden deseado y se cambia el orden
nuevas_columnas = [col for col in df.columns if col not in ['activo-1c', 'activo-2c', 'abandono']] + ['activo-1c', 'activo-2c', 'abandono']
df = df[nuevas_columnas]

print('Se exportan a results/dataset.xlsx para los datos procesados.')
df.to_excel('results/dataset.xlsx', index=False)

print('Procesamiento finalizado.')
