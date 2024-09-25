from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import json
import time
import re

# URL de la página inicial
Pagina_Url = "https://www.apple.com/careers/us/index.html"

# Inicializar el driver
driver = webdriver.Chrome()

# Lista para almacenar los trabajos
trabajos = []

# Acceder a la URL
driver.get(Pagina_Url)

try:
    # Esperar hasta que el primer link esté disponible y hacer clic
    link_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.more[href='/careers/us/software-and-services.html']")))
    link_button.click()

    # Esperar hasta que el segundo link esté disponible y hacer clic
    second_link_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href='https://jobs.apple.com/en-us/search?location=United-States-USA&team=Apps-and-Frameworks-SFTWR-AF']")))
    second_link_button.click()

    # Bucle para navegar por todas las páginas
    while True:
        # Esperar a que los trabajos se carguen
        job_links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.arrow.arrow--blue.arrow--14")))

        # Guardar los href de cada trabajo
        job_urls = [link.get_attribute('href') for link in job_links]

        # Iterar sobre cada trabajo
        for job_url in job_urls:
            # Hacer clic en el botón para mostrar el equipo
            teams_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "teams-filter-acc")))
            teams_button.click()

            time.sleep(1)  # Esperar un momento para permitir que el contenido se cargue

            try:
                title = driver.find_element(By.CSS_SELECTOR, "span.filters-list__title").text.strip()
            except:
                title = "Null"
            try:
                team = driver.find_element(By.CSS_SELECTOR, "span.teams-filter-checklst").text.strip()
            except:
                team = "Null"

            driver.get(job_url)

            # Esperar un poco para que se cargue la página completa
            time.sleep(3)

            # Recopilar los datos
            try:
                job_category = driver.find_element(By.ID, "job-team-name").text.strip()
                job_title = driver.find_element(By.ID, "jdPostingTitle").text.strip()
                job_location = driver.find_element(By.ID, "job-location-name").text.strip()
                role_number = driver.find_element(By.ID, "jobNumber").text.strip()
                summary = driver.find_element(By.ID, "jd-job-summary").text.strip()
                description = driver.find_element(By.ID, "jd-description").text.strip()

                # Posted Date
                posted_date = driver.find_element(By.ID, "jobPostDate").get_attribute('datetime').strip()
                print(f"Posted Date: {posted_date}")

                # Transformar el formato de la fecha
                try:
                    date_object = datetime.strptime(posted_date, "%Y-%m-%d")
                    formatted_date = date_object.strftime("%Y%m%d")  # Convertir a yyyyMMdd
                    print(f"Formatted Posted Date: {formatted_date}")
                except ValueError as e:
                    print(f"Error al transformar la fecha: {e}")

                role_number = driver.find_element(By.ID, "jobNumber").text.strip()
                summary = driver.find_element(By.ID, "jd-job-summary").text.strip()
                description = driver.find_element(By.ID, "jd-description").text.strip()

                # Intentar extraer "Key Qualifications"
                try:
                    key_qualifications = driver.find_element(By.ID, "jd-key-qualifications").text.strip()
                    print(f"key_qualifications: {key_qualifications}")
                except Exception:
                    key_qualifications = None  # Si no está disponible, establecer como None

                    # Si "Key Qualifications" no está disponible, intentar extraer "Preferred Qualifications"
                if not key_qualifications:
                    try:
                        preferred_qualifications = driver.find_element(By.ID, "jd-minimum-qualifications").text.strip()
                        print(f"preferred_qualifications: {preferred_qualifications}")
                    except Exception:
                        preferred_qualifications = None
                        print("No se encontraron 'Key Qualifications' ni 'Preferred Qualifications'.")

                # pay_benefits
                try:
                    # Esperar hasta que el elemento esté presente en el DOM
                    pay_benefits_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.ID, "accordion_pay&benefits"))
                    )
                    pay_benefits = pay_benefits_element.text.strip()

                    # Utilizar una expresión regular para encontrar los números en el rango de salarios
                    salario_regex = re.search(r'\$([\d,]+) and \$([\d,]+)', pay_benefits)

                    if salario_regex:
                        salario_min = salario_regex.group(1)  # El primer número del rango (valor mínimo)
                        salario_min = salario_min.replace(',', '')  # Remover las comas
                        salario_min = int(salario_min)  # Convertir a entero

                        salario_max = salario_regex.group(2)  # El segundo número del rango (valor máximo)
                        salario_max = salario_max.replace(',', '')  # Remover las comas
                        salario_max = int(salario_max)  # Convertir a entero

                        print(f"Salario Mínimo: {salario_min}")  # Ahora mostrará solo el número
                        print(f"Salario Máximo: {salario_max}")  # Muestra solo el número
                    else:
                        print("No se encontró el rango de salario en el texto.")
                        salario_min = 0
                        salario_max = 0
                except Exception as e:
                    print(f"Error al obtener Pay & Benefits:")
                    salario_min = 0
                    salario_max = 0

                # Crear un diccionario con los datos
                trabajo = {
                    "Title": title,
                    "Team": team,
                    "Job Category": job_category,
                    "Job Title": job_title,
                    "Job Location": job_location,
                    "Posted Date": formatted_date,
                    "Role Number": role_number,
                    "Summary": summary,
                    "Description": description,
                    "Key Qualifications": key_qualifications if key_qualifications else preferred_qualifications,
                    "Salario Mínimo": salario_min,
                    "Salario Máximo": salario_max,
                    "Job URL": job_url
                }

                # Agregar el trabajo a la lista
                trabajos.append(trabajo)

            except Exception as e:
                print(f"Error al obtener la información: {e}")

            # Regresar a la página anterior
            driver.back()
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.arrow.arrow--blue.arrow--14")))

        # Intentar encontrar el enlace de la siguiente página
        try:
            next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li.pagination__next a")))
            next_page_button.click()
            time.sleep(3)  # Esperar a que se carguen los nuevos trabajos

        except Exception:
            print("No hay más páginas para procesar.")
            break

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    # Guardar los trabajos en un archivo JSON
    with open('trabajos.json', 'w') as archivo_json:
        json.dump(trabajos, archivo_json, indent=4)

    # Cerrar el driver
    driver.quit()

    print(f'Datos almacenados en trabajos.json')
