import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# --- Gestión del WebDriver ---
# Se utiliza ChromeDriverManager para descargar e instalar automáticamente el driver de Chrome.
driver_path = ChromeDriverManager().install()

# Corrección de la ruta del binario:
# En algunos casos, la librería puede devolver la ruta a un archivo de texto de licencia 
# en lugar del binario 'chromedriver'. Aquí verificamos y corregimos la ruta si es necesario.
if os.path.basename(driver_path) != "chromedriver":
    dir_path = os.path.dirname(driver_path)
    binary_path = os.path.join(dir_path, "chromedriver")
    if os.path.exists(binary_path):
        driver_path = binary_path

# Otorgar permisos de ejecución al driver (necesario en macOS/Linux para evitar errores de permisos).
os.chmod(driver_path, 0o755)

# --- Inicialización del Navegador ---
# Se crea la instancia del navegador utilizando el servicio con la ruta corregida.
driver = webdriver.Chrome(service=Service(driver_path))

# --- Secuencia de Navegación de Prueba ---
# 1. Abrir Google
driver.get("https://www.google.com")
sleep(2) # Pausa de 2 segundos para visualización

# 2. Abrir el sitio de Hybridge Education
driver.get("https://hybridge.education")
sleep(2)

# 3. Abrir el sitio de OpenAI
driver.get("https://openai.com")