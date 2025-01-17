import pandas as pd
import os
import shutil
from datetime import datetime
import subprocess  # Para ejecutar el archivo .bat

# Cargar el archivo Excel
archivo_excel = '../Resultado/f1_actualizado.xlsx'
df = pd.read_excel(archivo_excel)

# Guardar el archivo en formato CSV con delimitador ';' y codificación 'utf-8-sig'
archivo_csv = '../Resultado/f1_actualizado.csv'
df.to_csv(archivo_csv, sep=';', index=False, encoding='utf-8-sig')

# Obtener la fecha actual en formato AAAAMMDD
fecha_actual = datetime.now().strftime('%Y%m%d')

# Cambiar la extensión del archivo a .sti con la fecha actual
archivo_sti = f'../Resultado/f1_actualizado_{fecha_actual}.sti'

# Si el archivo .sti ya existe en el directorio actual, eliminarlo
if os.path.exists(archivo_sti):
    os.remove(archivo_sti)
    print(f'Archivo existente eliminado: {archivo_sti}')

# Renombrar el archivo a .sti con la fecha
os.rename(archivo_csv, archivo_sti)

print(f'Archivo convertido a {archivo_sti} con delimitador ";" y codificación UTF-8-SIG')

# Detectar si la unidad S: está disponible
unidad_red = r'S:\Cmdb\1'
ruta_unc = r'\\servidor\Cmdb\1'

# Ruta destino inicial (intentar primero con la unidad de red)
if os.path.exists(unidad_red):
    directorio_destino = unidad_red
    print(f"Usando la unidad de red: {unidad_red}")
else:
    directorio_destino = ruta_unc
    print(f"Usando la ruta UNC: {ruta_unc}")

# Función para mover el archivo
def mover_archivo(origen, destino):
    try:
        ruta_destino = os.path.join(destino, os.path.basename(origen))
        shutil.move(origen, ruta_destino)  # Intenta mover el archivo
        print(f'Archivo movido a {ruta_destino}')
        return True  # Indica que el movimiento fue exitoso
    except Exception as e:
        print(f'Error al mover el archivo: {e}')
        return False  # Indica que el movimiento falló

# Intentar mover el archivo al directorio destino
if not mover_archivo(archivo_sti, directorio_destino):
    print("El primer intento de mover el archivo falló. Intentando conectar la unidad de red...")

    # Ejecutar el archivo .bat para establecer las credenciales de red
    bat_file = r'..\Si_no_va\Conectar_unidad_de_red.bat'  # Ruta al archivo .bat
    if os.path.exists(bat_file):
        try:
            subprocess.run([bat_file], check=True, shell=True)  # Ejecuta el archivo .bat
            print(f"Credenciales de red configuradas con éxito usando {bat_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el archivo .bat: {e}")

    # Intentar mover el archivo nuevamente después de conectar la unidad de red
    if not mover_archivo(archivo_sti, directorio_destino):
        print("No se pudo mover el archivo después de intentar conectar la unidad de red. Verifique los permisos o la conectividad.")
