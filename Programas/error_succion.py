import os
import time
from datetime import datetime

# Directorio de logs
directorio_logs = r'S:\Cmdb\1\logs'

# Ruta del archivo log
ruta_log_error = '../Logs/log_error_succion.txt'

def pausa_15_minutos():
    print("Esperando 15 minutos antes de iniciar...")
    time.sleep(900)  # 15 minutos en segundos
def obtener_archivo_mas_reciente(directorio):
    try:
        # Listar archivos en el directorio
        archivos = [os.path.join(directorio, archivo) for archivo in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, archivo))]
        # Obtener el archivo más reciente
        archivo_mas_reciente = max(archivos, key=os.path.getmtime)
        return archivo_mas_reciente
    except Exception as e:
        print(f"Error al listar archivos: {e}")
        return None

def procesar_nombre_archivo(archivo):
    # Ignorar los primeros 21 caracteres del nombre del archivo
    nombre_archivo = os.path.basename(archivo)
    nombre_procesado = nombre_archivo[22:]
    return nombre_procesado

def comparar_archivos(archivo_procesado, nombre_referencia):
    if archivo_procesado == nombre_referencia:
        print(f"El archivo coincide con el nombre de referencia: {nombre_referencia}")
        return True
    else:
        print(f"El archivo no coincide. Procesado: {archivo_procesado}, Referencia: {nombre_referencia}")
        return False

def registrar_estado_log(ruta_log, estado):
    try:
        with open(ruta_log, 'w') as log_file:
            log_file.write(f"error_detectado={str(estado)}\n")
        print(f"Estado registrado en el log: error_detectado={str(estado)}")
    except Exception as e:
        print(f"Error al escribir en el log: {e}")

if __name__ == "__main__":
    pausa_15_minutos()
    
    archivo_mas_reciente = obtener_archivo_mas_reciente(directorio_logs)
    
    if archivo_mas_reciente:
        print(f"Archivo más reciente encontrado: {archivo_mas_reciente}")
        archivo_procesado = procesar_nombre_archivo(archivo_mas_reciente)
        
        # Generar el nombre de referencia basado en la fecha actual
        fecha_actual = datetime.now().strftime('%Y%m%d')
        nombre_referencia = f"f1_actualizado_{fecha_actual}.log"
        
        # Comparar nombres
        if comparar_archivos(archivo_procesado, nombre_referencia):
            registrar_estado_log(ruta_log_error, True)
        else:
            registrar_estado_log(ruta_log_error, False)
    else:
        registrar_estado_log(ruta_log_error, False)
