import pandas as pd
import os

# Cargar el archivo Excel
archivo_csv = '../Archivo_uso/servicetonic.csv'
df = pd.read_csv(archivo_csv, sep=';', encoding='utf-8')

# Guardar el archivo en formato CSV con delimitador ';' y codificación 'utf-8-sig'
archivo_excel = '../Archivo_uso/servicetonic.xlsx'
df.to_excel(archivo_excel, index=False, engine='openpyxl')

print('Csv formatado correctamente a Excel')
