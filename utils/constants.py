# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:48:17 2023

@author: jumaf
"""


COLUMNAS_COMUNES =  [
    'documento', 'carrera', 'cr', '1-mi_grupo_familiar', '1-compañeras/os_o_amigas/os', '1-algún_pariente',
    '1-familia_amiga_de_mi_familia', '1-sola/o', '1-otros_(especificar)', '2-a_pie', '2-en_bicicleta_o_moto',
    '2-en_tren', '2-en_colectivo_de_corta_distancia', '2-en_colectivo_de_media_distancia',
    '2-en_colectivo_de_larga_distancia', '2-en_colectivo_o_combi_contratada', '2-en_auto', '2-otros_(especificar)',
    '3-minutos', '4-mucho', '4-poco', '4-nada', '5-no_se_toma_examen_de_ingreso', '5-es_gratuita',
    '5-se_dicta_la_carrera_que_prefiero', '5-por_la_cercanía', '5-me_la_recomendaron', '5-por_su_calidad_académica',
    '5-por_el_prestigio_de_la_carrera', '5-otras_razones', '6-medio_o_forma_por_el_cual_conoció_la_universidad',
    '7-si', '7-no', '8-medio/polimodal', '8-terciario', '8-universitario', '9-primario', '9-medio/polimodal',
    '9-terciario', '9-universitario', '10-público', '10-privado',
    '11-escuela_de_educación_media_(polimodal,_ex-comercial,_ex-normal_o_nacional)', '11-escuela_de_educación_técnica_(ex-enet)',
    '11-escuela_de_educación_agraria_(eea)', '11-cens', '11-otros_(especificar)', '12-número_del_colegio', '13-nombre_del_colegio',
    '14-país', '14-provincia', '14-partido/depto', '15-bachiller', '15-técnico', '15-otro_(especificar)', '16-descripción', '17-si',
    '17-no', '18-si', '18-no', '19-si', '19-no', '20-total', '20-parcial', '20-ninguna', '21-obrero_o_empleado',
    '21-cuenta_propista', '21-patrón_o_encargado', '21-trabajador_familiar', '22-agropecuaria', '22-industrial', '22-comercio',
    '22-educación', '22-turismo', '22-servicios_públicos', '22-servicios_privados', '22-otras_(especificar)', '23-formal', '23-informal',
    '24-permanente', '24-temporario', '25-menos_de_10_horas', '25-de_25_a_48_horas', '25-de_11_a_24_horas', '25-más_de_48_horas',
    '26-fijos', '26-rotativos', '27-mañana', '27-tarde', '27-noche', '28-siempre_que_sea_necesario', '28-sólo_algunas_veces',
    '28-nunca', '29-si', '29-no', '30-padre', '30-madre', '30-hermanas/os', '30-abuelas/os', '30-esposa/o_o_pareja', '30-hijas/os',
    '30-sobrinas/os', '30-amigas/os', '30-vivo_sola/o', '30-otros_(especificar)', '31-especificar', '32-universitarios',
    '32-terciario_no_universitario', '32-medio_o_polimodal', '32-primario_o_egb', '33-trabajan', '33-tienen_planes_trabajar_o_similares',
    '33-no_trabajan_pero_estan_buscando_trabajo', '33-no_trabajan_porque_estudian', '33-no_trabajan_y_no_están_buscando',
    '33-son_jubilados_o_pensionados', '34-madre', '34-padre', '35-si', '35-no', '36-inglés', '36-portugués', '36-francés',
    '36-otros', '36-especificar', '37-tu_casa', '37-tu_trabajo', '37-otros', '37-especificar', '38-procesador_de_texto',
    '38-planilla_de_cálculo', '38-navegación_por_internet', '38-otros', '38-especificar', 'cohorte'
]

COLUMNAS_NO_REEMPLAZAN_VALOR = ['documento', 'carrera', 'cr', '1-otros_(especificar)', '2-otros_(especificar)', '3-minutos', '5-no_se_toma_examen_de_ingreso', '5-es_gratuita', '5-se_dicta_la_carrera_que_prefiero',
'5-por_la_cercanía', '5-me_la_recomendaron', '5-por_su_calidad_académica', '5-por_el_prestigio_de_la_carrera', '5-otras_razones', '11-otros_(especificar)'
'12-número_del_colegio', '13-nombre_del_colegio', '14-país', '14-provincia', '14-partido/depto', '15-otro_(especificar)', '16-descripción', '22-otras_(especificar)',
'30-otros_(especificar)', '31-especificar', '32-universitarios', '32-terciario_no_universitario', '32-medio_o_polimodal', '32-primario_o_egb', '33-trabajan', 
'33-tienen_planes_trabajar_o_similares', '33-no_trabajan_pero_estan_buscando_trabajo', '33-no_trabajan_porque_estudian', '33-no_trabajan_y_no_están_buscando',
'33-son_jubilados_o_pensionados', '34-madre', '34-padre', '36-inglés', '36-portugués', '36-francés', '36-otros', '36-especificar', '37-tu_casa',
'37-tu_trabajo', '37-otros', '37-especificar', '38-procesador_de_texto', '38-planilla_de_cálculo', '38-navegación_por_internet', '38-otros',
'38-especificar', 'cohorte']

PREGUNTAS_PARA_AGRUPAR = [1, 2, 4, 7, 8, 9, 10, 11, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 35]

# Nombre de la columna a cambiar
COLUMNA_A_CAMBIAR = '33-no_trabajan_pero_est&aacuten_buscando_trabajo'
NUEVO_NOMBRE_COLUMNA = '33-no_trabajan_pero_estan_buscando_trabajo'
