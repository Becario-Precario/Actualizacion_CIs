from sqlalchemy import create_engine
import pandas as pd

# Configuración de conexión
servidor = '192.168.5.203'  # Dirección IP del servidor SQL Server
base_datos = 'dbst'  # Nombre de la base de datos
usuario = 'administrador'  # Usuario SQL creado en la instancia
contrasena = 'uv3O837JZC'  # Contraseña del usuario SQL

# Crear la cadena de conexión
conexion_str = f"mssql+pyodbc://{usuario}:{contrasena}@{servidor}/{base_datos}?driver=ODBC+Driver+17+for+SQL+Server"

try:
    # Crear el motor de conexión
    engine = create_engine(conexion_str)
    print("Conexión exitosa a la base de datos.")

    # Consulta SQL
    consulta_sql = """
    SELECT SERIAL_NUMBER, TITLE, STATUS, Part_number, Descripcion, suscription_id, FechaActivacion, FechaVencimiento, EmpresaCI, cantidad, coste, pvp2, pvp_total, tipo_facturacion, mail_contacto, val , autorenovable
    FROM configuration_item ci
    LEFT JOIN configuration_item_0001 c1 
    ON ci.ID_CI = c1.ID_CI
    WHERE CI_TYPE = 'Licencia_m365';
    """
    
    # Ejecutar la consulta y cargar en un DataFrame
    df = pd.read_sql_query(consulta_sql, con=engine)
    print("Consulta ejecutada correctamente.")
    
    # Ruta para guardar el archivo CSV
    archivo_csv = r"C:\Users\Administrador\Documents\Python\Archivo_uso\servicetonic.csv"  # Ruta de salida del archivo CSV
    
    # Guardar los resultados en un archivo CSV
    df.to_csv(archivo_csv, sep=';', index=False, encoding='utf-8-sig')
    print(f"Archivo CSV guardado exitosamente en: {archivo_csv}")

except Exception as e:
    print(f"Error al ejecutar el script: {e}")
