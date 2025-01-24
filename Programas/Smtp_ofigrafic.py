import smtplib  # Importa el módulo para manejar conexiones SMTP y enviar correos electrónicos.
from email.mime.multipart import MIMEMultipart  # Permite crear mensajes con múltiples partes.
from email.mime.text import MIMEText  # Permite agregar texto al correo electrónico.
from email.mime.base import MIMEBase  # Permite adjuntar archivos al correo electrónico.
from email import encoders  # Utilizado para codificar los archivos adjuntos en formato base64.
import os  # Módulo para interactuar con el sistema de archivos.
import time  # Módulo para manejar pausas temporales.
from datetime import datetime  # Módulo para manejar fechas y horas.

# Configuración del servidor SMTP
SMTP_SERVER =   # Dirección del servidor SMTP.
SMTP_PORT = 587  # Puerto del servidor SMTP para conexiones TLS.
SMTP_USER =   # Usuario para autenticarse en el servidor SMTP.
SMTP_PASSWORD =   # Contraseña del usuario SMTP.

# Direcciones de correo
FROM_EMAIL =  # Dirección del remitente.
TO_EMAIL =  # Dirección del destinatario principal.
CC_EMAIL = # Dirección de copia al destinatario.

'''
# Retraso de 15 minutos antes de enviar el correo
time.sleep(900)  # Pausa el programa durante 900 segundos (15 minutos).
'''

# Fecha y hora actual en el formato solicitado
fecha_actual = datetime.now().strftime("%d %B %Y %H:%M")  # Obtiene la fecha y hora actual en formato legible.

# Leer el estado de los correos
estado_correos = False
estado_log = '../Logs/log_status_correos.txt'
if os.path.exists(estado_log):
    with open(estado_log, 'r') as status_file:
        estado_correos = 'correos_vacios=True' in status_file.read()

# Leer el estado del error de succión
error_succion = False
error_log = '../Logs/error_succion.txt'
if os.path.exists(error_log):
    with open(error_log, 'r') as error_file:
        error_succion = 'error_succion=True' in error_file.read()

# Leer el contenido del log de correos si hay correos vacíos
contenido_log_emails = ""  # Variable para almacenar el contenido del log de correos.
if estado_correos:  # Si hay correos vacíos.
    log_emails_path = '../Logs/log_emails.txt'  # Ruta al archivo del log de correos.
    if os.path.exists(log_emails_path):  # Verifica si el archivo existe.
        with open(log_emails_path, 'r') as log_file:  # Abre el archivo para lectura.
            contenido_log_emails = log_file.read()  # Lee el contenido del archivo.

# Mensajes para las distintas combinaciones
if estado_correos and error_succion:
    SUBJECT = f"Proceso Automático: Correos Vacíos y Error de Succión - {fecha_actual}"
    BODY = (
        f"Estimado equipo,\n\n"
        f"El proceso automático se ha generado correctamente el día {fecha_actual}.\n\n"
        f"Sin embargo, se detectaron los siguientes problemas:\n"
        f"- Un error en el proceso de succión. Revise los detalles en el log adjunto de errores.\n"
        f"- Correos electrónicos vacíos que requieren revisión manual. Revise el log de correos adjunto.\n\n"
        f"Gracias por atender estas incidencias.\n\n"
        f"Saludos cordiales,\n"
        f"Equipo de Alanito"
    )
elif estado_correos:
    SUBJECT = f"Proceso Automático: Correos Vacíos - {fecha_actual}"
    BODY = (
        f"Estimado equipo,\n\n"
        f"El proceso automático se ha generado correctamente el día {fecha_actual}.\n\n"
        f"Sin embargo, se han detectado campos de correo vacíos que requieren revisión manual. Por favor, revise el log de correos adjunto para completar esta información.\n\n"
        f"Detalle del log de correos:\n"
        f"{contenido_log_emails}\n\n"
        f"Adicionalmente, se adjuntan los logs generales para que puedan verificar todos los cambios realizados durante el proceso.\n\n"
        f"Saludos cordiales,\n"
        f"Equipo de Alanito"
    )
elif error_succion:
    SUBJECT = f"Proceso Automático: Error de Succión - {fecha_actual}"
    BODY = (
        f"Estimado equipo,\n\n"
        f"El proceso automático se ha generado correctamente el día {fecha_actual}.\n\n"
        f"Sin embargo, se detectó un error en el proceso de succión. "
        f"Por favor, revise los detalles en el log adjunto de errores.\n\n"
        f"Gracias por atender esta incidencia.\n\n"
        f"Saludos cordiales,\n"
        f"Equipo de Alanito"
    )
else:
    SUBJECT = f"Proceso Automático Completado - {fecha_actual}"
    BODY = (
        f"Estimado equipo,\n\n"
        f"El proceso automático se ha generado correctamente el día {fecha_actual}.\n\n"
        f"Por favor, revise los logs adjuntos para verificar los cambios realizados y los detalles del proceso ejecutado.\n\n"
        f"Gracias.\n\n"
        f"Saludos cordiales,\n"
        f"Equipo de Alanito"
    )

# Archivos a adjuntar
logs = [
    '../Logs/log_1.txt',
    '../Logs/log_2.txt',
    '../Logs/fechas.txt',
    '../Logs/log_emails.txt',
    '../Logs/resultado_correo.csv',
    '../Logs/error_succion.txt'  
]
archivo_final = '../Resultado/f1_actualizado.xlsx'  # Archivo final que se adjuntará.

# Función para enviar el correo electrónico
def enviar_correo():
    try:
        mensaje = MIMEMultipart()  # Crea un objeto para el correo electrónico.
        mensaje['From'] = FROM_EMAIL  # Configura el remitente.
        mensaje['To'] = TO_EMAIL  # Configura el destinatario.
        mensaje['Cc'] = CC_EMAIL  # Configura la copia.
        mensaje['Subject'] = SUBJECT  # Configura el asunto.
        mensaje.attach(MIMEText(BODY, 'plain'))  # Adjunta el cuerpo del mensaje como texto plano.

        # Adjuntar los logs
        for log in logs:  # Itera sobre la lista de logs.
            if os.path.exists(log):  # Verifica si el archivo existe.
                with open(log, 'rb') as archivo:  # Abre el archivo en modo binario.
                    parte = MIMEBase('application', 'octet-stream')  # Crea una parte del correo para el archivo.
                    parte.set_payload(archivo.read())  # Carga el contenido del archivo.
                    encoders.encode_base64(parte)  # Codifica el archivo en base64.
                    parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(log)}')  # Agrega los encabezados necesarios.
                    mensaje.attach(parte)  # Adjunta el archivo al correo.

        # Adjuntar el archivo final
        if os.path.exists(archivo_final):  # Verifica si el archivo final existe.
            with open(archivo_final, 'rb') as archivo:  # Abre el archivo en modo binario.
                parte = MIMEBase('application', 'octet-stream')  # Crea una parte para el archivo.
                parte.set_payload(archivo.read())  # Carga el contenido del archivo.
                encoders.encode_base64(parte)  # Codifica el archivo en base64.
                parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(archivo_final)}')  # Agrega los encabezados.
                mensaje.attach(parte)  # Adjunta el archivo al correo.

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:  # Crea una conexión SMTP.
            servidor.starttls()  # Inicia la conexión TLS.
            servidor.login(SMTP_USER, SMTP_PASSWORD)  # Inicia sesión en el servidor SMTP.
            servidor.send_message(mensaje)  # Envía el mensaje.

        print("Correo enviado exitosamente.")  # Imprime un mensaje de éxito.

    except Exception as e:  # Maneja errores durante el envío del correo.
        print(f"Error al enviar el correo: {e}")  # Imprime el error.

# Ejecuta la función principal solo si el archivo se ejecuta directamente.
if __name__ == '__main__':
    enviar_correo()  # Llama a la función para enviar el correo.
