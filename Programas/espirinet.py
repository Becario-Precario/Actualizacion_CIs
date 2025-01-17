import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import shutil

# Configuración de las opciones del navegador Chrome
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    # Establece la ruta de descarga predeterminada
    "download.default_directory": r"C:\Users\Administrador\Documents\Python\Archivo_uso",
    "download.prompt_for_download": False,  # Evita que aparezca un cuadro de diálogo al descargar
    "download.directory_upgrade": True,  # Permite actualizar el directorio de descarga si ya existe
    "safebrowsing.enabled": True  # Habilita la navegación segura
})
chrome_options.add_argument("--start-maximized")  # Inicia el navegador en pantalla completa

# Inicia el controlador de Chrome con las opciones configuradas
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

try:
    # Abre la página de inicio de sesión de Esprinet
    driver.get("https://b2b.esprinet.com/Cloud/Home/Embedded")

    # Espera hasta que el campo de usuario esté disponible y lo rellena
    wait = WebDriverWait(driver, 40)  # Tiempo máximo de espera de 40 segundos
    username_input = wait.until(EC.presence_of_element_located((By.ID, "Username")))
    username_input.send_keys("1117325001")  # Ingresa el usuario (credenciales estáticas)

    # Espera hasta que el campo de contraseña esté disponible y lo rellena
    password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
    password_input.send_keys("Vilasok*96!!")  # Ingresa la contraseña (credenciales estáticas)
    password_input.send_keys(Keys.RETURN)  # Envía el formulario pulsando la tecla Enter

    # Pausa para asegurarse de que la sesión se ha iniciado correctamente
    time.sleep(10)  # Se puede mejorar usando una espera dinámica basada en la aparición de un elemento

    # Navega a la página de suscripciones activas
    driver.get("https://cloud.esprinet.com/Subscriptions?ProvisioningStatus=Active")
    print("Navegación a la página de suscripciones activas...")

    # Espera a que el botón de exportación esté visible y realiza clic
    export_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@ng-click, 'exportSubscriptions')]")))
    export_button.click()
    print("Botón de exportación clicado. Esperando descarga...")

    # Pausa para permitir que el archivo se descargue
    time.sleep(30)  # Ajustar según la velocidad de descarga

    # Renombra el archivo descargado
    download_folder = r"C:\Users\Administrador\Documents\Python\Archivo_uso"
    # Encuentra el archivo más reciente en la carpeta de descargas
    filename = max([os.path.join(download_folder, f) for f in os.listdir(download_folder)], key=os.path.getctime)
    # Establece el nuevo nombre del archivo
    new_file_path = os.path.join(download_folder, "proveedor.xlsx")
    shutil.move(filename, new_file_path)  # Mueve y renombra el archivo
    print("Archivo descargado y renombrado correctamente como 'proveedores.xlsx'.")

finally:
    # Cierra el navegador independientemente de si ocurre un error o no
    driver.quit()
