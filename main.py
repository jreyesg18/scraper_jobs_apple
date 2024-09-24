from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#Palabra_clave = input("Que buscas: ")
#Pagina_Url = input("Ingrese URL: ")
#navegador = input("Seleccione el navegador que desea utilizar:\n1. Chrome\n2. Firefox\nEscriba '1' o '2', o directamente 'Chrome' o 'Firefox': ").lower()

Pagina_Url ="https://www.apple.com/careers/us/index.html"

driver = None

driver = webdriver.Chrome()

driver.get(Pagina_Url)

link_button = driver.find_element(By.CSS_SELECTOR, "a.more[href='/careers/us/software-and-services.html']")
link_button.click()

link_button = driver.find_element(By.CSS_SELECTOR, "a[href='https://jobs.apple.com/en-us/search?location=United-States-USA&team=Apps-and-Frameworks-SFTWR-AF']")
link_button.click()


'''
icon_button = driver.find_element(By.CSS_SELECTOR, "span.accordion-icon.icon.icon-after.icon-plus")
icon_button.click()
'''
# Esperar a que se carguen los tbody
time.sleep(3)  # Aumenta el tiempo si es necesario

# Extraer información de los tbody
tbodys = driver.find_elements(By.TAG_NAME, 'tbody')

for tbody in tbodys:

    tbody_id = tbody.get_attribute('id')  # Obtener el id del tbody
    rows = tbody.find_elements(By.TAG_NAME, 'tr')  # Encontrar todas las filas dentro del tbody

    print(f"Información del {tbody_id}:")
    for row in rows:

        # Extraer información de las columnas
        columns = row.find_elements(By.TAG_NAME, 'td')  # Encuentra todas las celdas
        row_data = [column.text.strip() for column in columns]  # Extrae el texto de cada celda

        # Imprime la información de la fila
        print(row_data)

        # Buscar el botón del acordeón dentro de la fila (si está presente)
        try:
            icon_button = row.find_element(By.CSS_SELECTOR, "span.accordion-icon.icon.icon-after.icon-plus")
            if icon_button.is_displayed() and icon_button.is_enabled():
                icon_button.click()  # Hacer clic en el botón del acordeón
                print(f"Haciendo clic en el botón de la fila: {row_data}")
            else:
                print("El botón no está visible o habilitado.")
        except Exception as e:
            print(f"No se pudo encontrar el botón del acordeón en la fila: {e}")

   # < a href = "/careers/us/hardware.html" class ="more" > Hardware < / a >

#driver.quit()
