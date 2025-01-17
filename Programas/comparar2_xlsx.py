import pandas as pd
import os
from datetime import datetime

# Eliminar archivos existentes para asegurar que se crean de nuevo
for file in ['../Logs/status.txt', '../Logs/fecha_inicio.txt', '../Logs/fecha_fin.txt', '../Logs/cantidad.txt', '../Logs/coste.txt', '../Logs/pvp2.txt', '../Logs/facturacion.txt', '../Logs/fechas_actualizacion.txt', '../Logs/log_emails.txt']:
    if os.path.exists(file):
        os.remove(file)

# Cargar los archivos Excel
f1_actualizado = pd.read_excel('../Resultado/f1_actualizado.xlsx')
f2 = pd.read_excel('../Archivo_uso/proveedor.xlsx')

# Alias de Sub_id
sub_id_alias = "Sub_id"

# Obtener la fecha actual
fecha_actual = datetime.now().date()

# Función para convertir una fecha al formato AAAAMMDD
def convertir_fecha(fecha):
    try:
        # Convierte la fecha al formato AAAAMMDD, si no está vacía
        if pd.notna(fecha):
            return pd.to_datetime(fecha, dayfirst=True).strftime('%Y%m%d')
        return fecha  # Deja el valor como está si es NaN
    except Exception as e:
        print(f"Error al convertir fecha {fecha}: {e}")
        return fecha

# Parte 1: Ir a f1_actualizado y actualizar la columna 3 con los valores de f2 columna 9
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 8]  # Suponiendo que col9 en f2 es el valor a comparar
        f1_value = row.iloc[2]  # Col3 en f1_actualizado
        
        # Determinar nuevo status
        new_status = 'active' if str(f2_value).strip().lower() in ['activa', 'active'] else 'inactive'
        
        if f1_value.lower() != new_status:
            # Documentar el cambio en status.txt
            with open('../Logs/status.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | status: {f1_value} --> {new_status}\n")
            
            # Actualizar f1_actualizado con el nuevo status
            f1_actualizado.at[index, f1_actualizado.columns[2]] = new_status

# Parte 2: Ir a f1_actualizado y actualizar la columna 7 con los valores de f2 columna 6
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 5]  # Suponiendo que col6 en f2 es el valor a comparar
        f1_value = row.iloc[6]  # Col7 en f1_actualizado
        
        new_value = f"{f2_value}.000" if pd.notna(f2_value) else ''
        
        if f1_value != new_value:
            # Documentar el cambio en fecha_inicio.txt
            with open('../Logs/fecha_inicio.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | fecha inicio: {f1_value} --> {new_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[6]] = new_value

# Parte 3: Ir a f1_actualizado y actualizar la columna 8 con los valores de f2 columna 7
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 6]  # Suponiendo que col7 en f2 es el valor a comparar
        f1_value = row.iloc[7]  # Col8 en f1_actualizado
        
        if pd.isna(f2_value):
            continue
        
        new_value = f"{f2_value}.000"
        
        if f1_value != new_value:
            # Documentar el cambio en fecha_fin.txt
            with open('../Logs/fecha_fin.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | fecha fin: {f1_value} --> {new_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[7]] = new_value

# Parte 4: Ir a f1_actualizado y actualizar la columna 10 con los valores de f2 columna 13
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    part_number_f1 = row.iloc[3]  # Suponiendo que col4 en f1_actualizado es el Part_Number
    
    # Ignorar si Part_Number empieza por 'csp' o 'CSP'
    if str(part_number_f1).lower().startswith('csp'):
        continue
    
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 12]  # Suponiendo que col13 en f2 es el valor a comparar
        f1_value = row.iloc[9]  # Col10 en f1_actualizado
        
        if f1_value != f2_value:
            # Documentar el cambio en cantidad.txt
            with open('../Logs/cantidad.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | cantidad: {f1_value} --> {f2_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[9]] = f2_value

# Parte 5: Ir a f1_actualizado y actualizar la columna 11 con los valores de f2 columna 14
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    part_number_f1 = row.iloc[3]  # Suponiendo que col4 en f1_actualizado es el Part_Number
    
    # Ignorar si Part_Number empieza por 'csp' o 'CSP'
    if str(part_number_f1).lower().startswith('csp'):
        continue
    
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 13]  # Suponiendo que col14 en f2 es el valor a comparar
        f1_value = row.iloc[10]  # Col11 en f1_actualizado
        
        if f1_value != f2_value:
            # Documentar el cambio en coste.txt
            with open('../Logs/coste.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | coste: {f1_value} --> {f2_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[10]] = f2_value

# Parte 6: Ir a f1_actualizado y actualizar la columna 12 con los valores de f2 columna 15
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    part_number_f1 = row.iloc[3]  # Suponiendo que col4 en f1_actualizado es el Part_Number
    
    # Ignorar si Part_Number empieza por 'csp' o 'CSP'
    if str(part_number_f1).lower().startswith('csp'):
        continue
    
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 14]  # Suponiendo que col15 en f2 es el valor a comparar
        f1_value = row.iloc[11]  # Col12 en f1_actualizado
        
        if f1_value != f2_value:
            # Documentar el cambio en pvp2.txt
            with open('../Logs/pvp2.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | pvp2: {f1_value} --> {f2_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[11]] = f2_value

# Parte 7: Ir a f1_actualizado y actualizar la columna 13 con la multiplicación de los valores de las columnas 10 y 12
for index, row in f1_actualizado.iterrows():
    valor_col10 = row.iloc[9]  # Col10 en f1_actualizado
    valor_col12 = row.iloc[11]  # Col12 en f1_actualizado
    
    if pd.notna(valor_col10) and pd.notna(valor_col12):
        try:
            new_value = float(valor_col10) * float(valor_col12)
        except ValueError:
            new_value = ''
    else:
        new_value = ''
    
    f1_actualizado.at[index, f1_actualizado.columns[12]] = new_value

# Parte 8: Ir a f1_actualizado y actualizar la columna 14 con los valores de f2 columna 11
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    part_number_f1 = row.iloc[3]  # Suponiendo que col4 en f1_actualizado es el Part_Number
    
    # Ignorar si Part_Number empieza por 'csp' o 'CSP'
    if str(part_number_f1).lower().startswith('csp'):
        continue
    
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 10]  # Suponiendo que col11 en f2 es el valor a comparar
        f1_value = row.iloc[13]  # Col14 en f1_actualizado
        
        new_value = f2_value
        
        # Validar si la columna 7 está vacía, contiene un valor nulo o espacios en blanco
        if pd.isna(row.iloc[7]) or str(row.iloc[7]).strip() in ['', '---']:
            new_value = 'Perpetua'
        
        if f1_value != new_value:
            # Documentar el cambio en facturacion.txt
            with open('../Logs/facturacion.txt', 'a') as f:
                f.write(f"Linea {index+2} | Valor ref: {sub_id_f1} | facturacion: {f1_value} --> {new_value}\n")
            
            # Actualizar f1_actualizado con el nuevo valor
            f1_actualizado.at[index, f1_actualizado.columns[13]] = new_value

# Parte 9: Ir a f1_actualizado y comparar la columna 8 con la fecha actual del sistema
for index, row in f1_actualizado.iterrows():
    fecha_col8 = row.iloc[7]  # Col8 en f1_actualizado
    status_col3 = row.iloc[2]  # Col3 en f1_actualizado
    
    if pd.notna(fecha_col8) and not str(fecha_col8).lower() in ['perpetua', '---']:
        try:
            fecha_col8_date = datetime.strptime(str(fecha_col8)[:10], '%Y-%m-%d').date()
            if fecha_col8_date < fecha_actual and status_col3.lower() != 'inactive':
                # Documentar el cambio en fechas_actualizacion.txt
                with open('../Logs/fechas_actualizacion.txt', 'a') as f:
                    f.write(f"Linea {index+2} | Valor ref: {row.iloc[5]} | fechas_actualizacion: {status_col3} --> inactive\n")
                
                # Actualizar f1_actualizado con el nuevo valor
                f1_actualizado.at[index, f1_actualizado.columns[2]] = 'inactive'
        except ValueError:
            pass
        
# Cambiar el tipo de la columna 17 de f1_actualizado a bool
f1_actualizado[f1_actualizado.columns[16]] = f1_actualizado[f1_actualizado.columns[16]].astype(bool)

# Parte 10: Rellenar col17 de f1 con col18 de f2
for index, row in f1_actualizado.iterrows():
    sub_id_f1 = row.iloc[5]  # Suponiendo que col6 en f1_actualizado es el Sub_id
    f2_match = f2[f2.iloc[:, 2] == sub_id_f1]  # Suponiendo que col3 en f2 es el Sub_id
    
    if not f2_match.empty:
        f2_value = f2_match.iloc[0, 17]  # Suponiendo que col18 en f2 es el valor a usar
        new_value = str(f2_value).strip().lower() in ['si', 'sí']
        
        # Actualizar f1_actualizado con el nuevo valor
        f1_actualizado.at[index, f1_actualizado.columns[16]] = new_value

# Parte 11: Completar correos electrónicos faltantes usando el nombre de la empresa
with open('../Logs/log_emails.txt', 'a') as log_file:
    log_file.write("Una lista de correos electrónicos actualizados y los que quedaron vacíos en servicetonic.xlsx.\n")
    log_file.write(f"Actualización de correos - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

    for index, row in f1_actualizado.iterrows():
        email_col = row.iloc[14]  # Columna 15 (email)
        company_col = row.iloc[8]  # Columna 9 (nombre empresa)

        if pd.isna(email_col) or (isinstance(email_col, str) and email_col.strip() == ''):
            # Buscar todas las filas que coincidan con el nombre de la empresa
            matching_rows = f1_actualizado[f1_actualizado.iloc[:, 8] == company_col]

            # Si hay coincidencias, buscar un correo válido
            for _, match_row in matching_rows.iterrows():
                matching_email = match_row.iloc[14]
                if pd.notna(matching_email) and isinstance(matching_email, str) and matching_email.strip() != '':
                    # Actualizar el correo faltante
                    old_email = email_col if pd.notna(email_col) else "(vacío)"
                    f1_actualizado.at[index, f1_actualizado.columns[14]] = matching_email

                    # Loggear la actualización con detalles del cambio
                    log_file.write(f"Linea {index+2} | Sub ID: {row.iloc[5]} | Email: {old_email} --> {matching_email}\n")
                    break

    # Listar líneas con correos aún vacíos
    log_file.write("\nNuevas suscripciones con el valor del Mail vacio. Revisar manualmente:\n")
    hay_correos_vacios = False
    for index, row in f1_actualizado.iterrows():
        email_col = row.iloc[14]  # Columna 15 (email)
        if pd.isna(email_col) or (isinstance(email_col, str) and email_col.strip() == ''):
            log_file.write(f"Linea {index+2} | Sub ID: {row.iloc[5]} | Empresa {row.iloc[8]}\n")
            hay_correos_vacios = True

    # Crear un archivo para registrar si hay correos vacíos
    with open('../Logs/log_status_correos.txt', 'w') as status_file:
        status_file.write("correos_vacios=True\n" if hay_correos_vacios else "correos_vacios=False\n")

    # Crear un DataFrame con las columnas requeridas
    resultado_df = pd.DataFrame({
        'Sub ID': f1_actualizado.iloc[:, 5].values,  # Columna 6 en Excel (Sub ID)
        'Empresa': f1_actualizado.iloc[:, 8].values,  # Columna 9 en Excel (nombre empresa)
        'Correo': f1_actualizado.iloc[:, 14].values  # Columna 15 en Excel (correo electrónico)
    })

    # Guardar el DataFrame como CSV con separador ';'
    resultado_df.to_csv('../Logs/resultado_correo.csv', index=False, sep=';', encoding='utf-8-sig')

    print("Archivo 'resultado_correo.csv' generado con éxito.")

            
# Convertir números con comas a puntos en las columnas 11, 12, y 13
def convert_comma_to_dot(value):
    if isinstance(value, str):
        value = value.replace(',', '.')
    try:
        value = float(value)
        return f"{value:.2f}"
    except ValueError:
        return value

for col in [10, 11, 12]:  # Columnas 11, 12 y 13 en f1_actualizado
    f1_actualizado.iloc[:, col] = f1_actualizado.iloc[:, col].apply(convert_comma_to_dot)

# Guardar el archivo actualizado
f1_actualizado.to_excel('../Resultado/f1_actualizado.xlsx', index=False)

# Consolidar archivos en log_1.txt y log_2.txt con las descripciones correspondientes
def consolidate_logs(file_list, output_file):
    file_descriptions = {
        '../Logs/valores_repetidos.txt': "Una lista de valores duplicados encontrados en las columnas específicas de servicetonic.xlsx y proveedor.xlsx.",
        '../Logs/temp_archivo1.txt': "Una lista del valor Sub_id en servicetonic.xlsx que no están en proveedor.xlsx.",
        '../Logs/temp_archivo2.txt': "Una lista del valor Sub_id en proveedor.xlsx que no están en servicetonic.xlsx.",
        '../Logs/part_number.txt': "Una lista de cambios realizados en los valores de Part_number en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/status.txt': "Una lista de cambios realizados en el estado de las suscripciones en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/fecha_inicio.txt': "Una lista de actualizaciones realizadas en los valores de FechaInicio en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/fecha_fin.txt': "Una lista de actualizaciones realizadas en los valores de FechaFin en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/cantidad.txt': "Una lista de cambios realizados en la cantidad de suscripciones en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/coste.txt': "Una lista de actualizaciones realizadas en los valores de Coste en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/pvp2.txt': "Una lista de cambios realizados en los valores de PVP2 en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/facturacion.txt': "Una lista de cambios realizados en el tipo de facturación en servicetonic.xlsx basados en proveedor.xlsx.",
        '../Logs/fechas_actualizacion.txt': "Una lista de cambios en el estado de las suscripciones basados en las fechas de vencimiento en servicetonic.xlsx.",
        '../Logs/log_emails.txt': "Una lista de correos electrónicos actualizados y los que quedaron vacíos en servicetonic.xlsx.",
        '../Logs/resultado_correo.csv': "Un archivo CSV con los datos consolidados de correos electrónicos para las empresas.",
        '../Logs/log_1.txt': "Una consolidación de valores duplicados y únicos en servicetonic.xlsx y proveedor.xlsx.",
        '../Logs/log_2.txt': "Una consolidación de los cambios realizados en status, cantidades, costes, y fechas en servicetonic.xlsx.",
        '../Logs/fechas.txt': "Una consolidación de las actualizaciones de FechaInicio y FechaFin en servicetonic.xlsx."
    }

    with open(output_file, 'w') as outfile:
        for fname in file_list:
            if os.path.exists(fname):
                # Escribir la descripción correspondiente antes del archivo
                description = file_descriptions.get(fname, "Descripción no disponible.")
                outfile.write(f"Descripción: {description}\n")
                outfile.write(f"Procesando el archivo: {fname}\n")
                with open(fname) as infile:
                    outfile.write(f"{fname}\n")  # Escribir nombre de archivo
                    outfile.write(infile.read())  # Escribir contenido del archivo
                    outfile.write("\n\n")
                os.remove(fname)

# Crear log_1.txt
consolidate_logs(['../Logs/valores_repetidos.txt', '../Logs/temp_archivo1.txt', '../Logs/temp_archivo2.txt'], '../Logs/log_1.txt')

# Crear log_2.txt
consolidate_logs(['../Logs/status.txt', '../Logs/cantidad.txt', '../Logs/coste.txt', '../Logs/pvp2.txt', '../Logs/facturacion.txt', '../Logs/fechas_actualizacion.txt'], '../Logs/log_2.txt')

# Consolidar fecha_inicio.txt y fecha_fin.txt en fechas.txt
consolidate_logs(['../Logs/fecha_inicio.txt', '../Logs/fecha_fin.txt'], '../Logs/fechas.txt')

# Función genérica para formatear fechas en una columna específica
def formatear_fecha_columna(df, indice_columna):
    df.iloc[:, indice_columna] = df.iloc[:, indice_columna].apply(convertir_fecha)

# Llamar a la función para formatear las columnas de fechas (índices 6 y 7)
formatear_fecha_columna(f1_actualizado, indice_columna=6)
formatear_fecha_columna(f1_actualizado, indice_columna=7)

# Guardar el archivo actualizado con las fechas formateadas
f1_actualizado.to_excel('../Resultado/f1_actualizado.xlsx', index=False)

print("Segunda comparacion realizada correctamente.")
