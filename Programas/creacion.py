import pandas as pd

# Función para leer valores de temp_archivo2.txt
def leer_temp_archivo(temp_archivo):
    with open(temp_archivo, 'r') as file:
        valores = [line.strip().split(' ')[1] for line in file]
    return valores

# Función para actualizar la primera columna con un contador
def actualizar_col1(df):
    contador_licencia = {}
    for index, row in df.iterrows():
        empresa = row.iloc[8][:10].replace(" ", "").upper()  # Ajustado para usar col9 (índice 8)
        contador = contador_licencia.get(empresa, 0) + 1
        contador_licencia[empresa] = contador
        nombre_personalizado = f"LIC{empresa}M365{contador}"
        df.at[index, df.columns[0]] = nombre_personalizado
    return df

# Actualizar el archivo servicetonic.xlsx con los valores del archivo temporal
def actualizar_f1(f1, f2, temp_archivo, f1_actualizado):
    try:
        df1 = pd.read_excel(f1)
        df2 = pd.read_excel(f2)

        # Asegurar que df1 tiene las columnas adicionales
        df1['autorenovable'] = df1.get('autorenovable', '')
        df1['CI_TYPE'] = df1.get('CI_TYPE', '')


        valores_temp = leer_temp_archivo(temp_archivo)
        
        nuevas_filas = []
        contador_licencia = {}

        # Generar nuevos registros basados en temp_archivo2.txt
        for valor in valores_temp:
            fila_f2 = df2[df2.iloc[:, 2] == valor]
            if not fila_f2.empty:
                fila_f2 = fila_f2.iloc[0]
                empresa = fila_f2.iloc[0][:10].replace(" ", "").upper()
                contador = contador_licencia.get(empresa, 0) + 1
                contador_licencia[empresa] = contador
                nombre_personalizado = f"LIC{empresa}M365{contador}"
                licencia_m365 = f"LICENCIA M365 {fila_f2.iloc[0].upper()}"
                nuevo_registro = [
                    nombre_personalizado,
                    licencia_m365,
                    fila_f2.iloc[8],
                    fila_f2.iloc[9],
                    fila_f2.iloc[4],
                    fila_f2.iloc[2],
                    f"{fila_f2.iloc[5]}.000" if pd.notna(fila_f2.iloc[5]) else '',
                    f"{fila_f2.iloc[6]}.000" if pd.notna(fila_f2.iloc[6]) else '',
                    fila_f2.iloc[0],
                    fila_f2.iloc[12],
                    fila_f2.iloc[13],
                    fila_f2.iloc[14],
                    fila_f2.iloc[15] if pd.notna(fila_f2.iloc[15]) else '',
                    fila_f2.iloc[10],
                    '',
                    0,
                    '',  # Dejar la columna 17 vacía
                    'Licencia_m365'  # CI_TYPE
                ]
                nuevas_filas.append(nuevo_registro)

        # Añadir nuevos registros a df1
        nuevas_filas_df = pd.DataFrame(nuevas_filas, columns=df1.columns)
        nuevas_filas_df.dropna(how='all', axis=0, inplace=True)  # Elimina filas vacías
        nuevas_filas_df.dropna(how='all', axis=1, inplace=True)  # Elimina columnas vacías
        df1_actualizado = pd.concat([df1, nuevas_filas_df], ignore_index=True)

        # Actualizar la primera columna de todos los registros
        df1_actualizado = actualizar_col1(df1_actualizado)

        # Actualizar la columna 18 de todos los registros con 'Licencia_m365'
        df1_actualizado['CI_TYPE'] = 'Licencia_m365'

        '''
        # Actualizar la mails si está vacía , actualizado en comparar2
        df1_actualizado[df1_actualizado.columns[14]] = df1_actualizado.groupby(df1_actualizado.columns[8])[df1_actualizado.columns[14]] \
            .transform(lambda x: x.bfill().ffill())
        '''

        # Guardar el archivo actualizado
        df1_actualizado.to_excel(f1_actualizado, index=False)

        print("Creacion de f1_actualizado.xlsx correctamente")
    
    except Exception as e:
        print(f"Error al actualizar f1: {e}")

# Ejecutar la función para actualizar f1
actualizar_f1('../Archivo_uso/servicetonic.xlsx', '../Archivo_uso/proveedor.xlsx', '../Logs/temp_archivo2.txt', '../Resultado/f1_actualizado.xlsx')
