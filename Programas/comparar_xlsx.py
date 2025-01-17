import pandas as pd
import os

# Eliminar archivos existentes para asegurar que se crean de nuevo
for file in ['../Logs/valores_repetidos.txt', '../Logs/log.txt', '../Logs/temp_archivo1.txt', '../Logs/temp_archivo2.txt', '../Logs/part_number.txt']:
    if os.path.exists(file):
        os.remove(file)

# Cargar los archivos Excel
f1 = pd.read_excel('../Archivo_uso/servicetonic.xlsx')
f2 = pd.read_excel('../Archivo_uso/proveedor.xlsx')

# Verificar si la columna "CIF/NIF " existe y eliminarla si está presente
if 'CIF/NIF' in f2.columns:
    f2.drop(columns=['CIF/NIF'], inplace=True)
    # Guardar el fichero después de eliminar la columna
    f2.to_excel('../Archivo_uso/proveedor.xlsx', index=False)
    


# Parte 1: Comparar la col6 del f1 y col3 del f2 con ellas mismas para detectar duplicados

# Función para encontrar valores duplicados en una columna y escribir en un archivo
def encontrar_duplicados(df, col_index, archivo, nombre_archivo):
    valores = df.iloc[:, col_index]
    duplicados = valores[valores.duplicated(keep=False)]
    if not duplicados.empty:
        with open(archivo, 'a') as f:
            f.write(f"Valores duplicados en {nombre_archivo}:\n")
            for valor, count in duplicados.value_counts().items():
                lineas = duplicados[duplicados == valor].index.tolist()
                lineas_str = ', '.join(map(lambda x: str(x+2), lineas))  # Sumar 2 a las líneas
                f.write(f"valor: {valor} {count} veces | Línea: {lineas_str}\n")
            f.write("\n")  # Añadir una línea en blanco al final del archivo para mejor formato

# Verificar duplicados en la col6 de f1
encontrar_duplicados(f1, 5, '../Logs/valores_repetidos.txt', '../Archivo_uso/servicetonic.xlsx')

# Verificar duplicados en la col3 de f2
encontrar_duplicados(f2, 2, '../Logs/valores_repetidos.txt', '../Archivo_uso/proveedor.xlsx')

# Parte 2: Comparar col6 de f1 con col3 de f2 y registrar valores únicos

valores_f1_col6 = f1.iloc[:, 5].drop_duplicates()
valores_f2_col3 = f2.iloc[:, 2].drop_duplicates()

# Valores en f1 col6 que no están en f2 col3
unicos_f1 = valores_f1_col6[~valores_f1_col6.isin(valores_f2_col3)]
with open('../Logs/temp_archivo1.txt', 'w') as f:
    for valor in unicos_f1:
        f.write(f"V: {valor}\n")

# Valores en f2 col3 que no están en f1 col6
unicos_f2 = valores_f2_col3[~valores_f2_col3.isin(valores_f1_col6)]
with open('../Logs/temp_archivo2.txt', 'w') as f:
    for valor in unicos_f2:
        f.write(f"V: {valor}\n")

# Parte 3: Comparar col6 de f1 con col3 de f2 y col4 de f1 con col10 de f2

comparaciones = []
for index, row in f1.iterrows():
    sub_id_f1 = row.iloc[5]
    part_number_f1 = row.iloc[3]
    f2_match = f2[(f2.iloc[:, 2] == sub_id_f1) & (f2.iloc[:, 9] == part_number_f1)]
    if not f2_match.empty:
        comparaciones.append((index, sub_id_f1, part_number_f1))

# Parte 4: Si Sub_id coincide pero Part_number no coincide, actualizar f1 con la información de f2

for index, row in f1.iterrows():
    sub_id_f1 = row.iloc[5]
    part_number_f1 = row.iloc[3]
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]
    if not f2_match.empty:
        for _, match_row in f2_match.iterrows():
            part_number_f2 = match_row.iloc[9]
            if part_number_f2.lower().startswith('csp'):
                continue  # Ignorar si Part_number empieza por 'csp' o 'CSP'
            if part_number_f1 != part_number_f2:
                f1.at[index, f1.columns[3]] = part_number_f2
                with open('../Logs/part_number.txt', 'a') as f:
                    f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | Part_number: {part_number_f1} --> {part_number_f2}\n")
                break  # Actualización hecha, salir del bucle

# Añadir columnas nuevas autorenovable y CI_TYPE
f1['autorenovable'] = ''
f1['CI_TYPE'] = ''

# Guardar archivo actualizado
f1.to_excel('../Archivo_uso/servicetonic.xlsx', index=False)

print("Primera comparacion correcta.")
