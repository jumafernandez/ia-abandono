# Descubrimiento de patrones de comportamiento vinculados al abandono en la UNLu mediante la aplicación de técnicas de _machine learning_
 
Scripts e información del Proyecto de Investigación PI2+ categoría A del Departamento de Ciencias Básicas "Descubrimiento de patrones de comportamiento vinculados al abandono en la Universidad Nacional de Luján mediante la aplicación de técnicas de aprendizaje automático".

## Forma de utilización:

### procesamiento_encuestas.py
1. Se deben descargar las encuestas socio-económicas que se desean procesar y persistirlas en un DIRECTORIO que será configurado en el archivo `utils/config.py`.
2. Luego, se ejecutra el script, el cual persistirá el reporte `results/encuestas-procesadas.xlsx` en el directorio `results`.

### notebook-eda.ipynb
1. En función del procesamiento anterior, se ejecuta la notebook.
2. Quedarán dos reportes disponibles en la siguiente ubicación: `reporte-eda-1.html` y `reporte-eda-2.html`.

### unificar_activos.py
1. Se deben persistir los datos de los activos en el directorio `/activos-por-anio'`.
2. Luego, se ejecuta el script, el cual persistirá los estudiantes de las cohortes COHORTE_DESDE a COHORTE_HASTA en `results/activos-procesadas-{COHORTE_DESDE}-{COHORTE_HASTA}.xlsx`.

### mix-info.py
1. Este script integra los datos preprocesados de las encuestas y los datos preprocesados de los activos.
2. Se ejecuta en última instancia, una vez ejecutados los scripts `procesamiento_encuestas.py` y `unificar_activos.py`.
