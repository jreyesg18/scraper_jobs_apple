from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL de la página inicial
Pagina_Url = "https://www.apple.com/careers/us/index.html"

# Inicializar el driver
driver = webdriver.Chrome()

# Acceder a la URL
driver.get(Pagina_Url)

try:
    # Esperar hasta que el primer link esté disponible y hacer clic
    link_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.more[href='/careers/us/software-and-services.html']"))
    )
    link_button.click()

    # Esperar hasta que el segundo link esté disponible y hacer clic
    second_link_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    "a[href='https://jobs.apple.com/en-us/search?location=United-States-USA&team=Apps-and-Frameworks-SFTWR-AF']"))
    )
    second_link_button.click()

    # Esperar a que los trabajos se carguen
    job_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.arrow.arrow--blue.arrow--14"))
    )

    # Guardar los href de cada trabajo
    job_urls = [link.get_attribute('href') for link in job_links]

    # Iterar sobre cada trabajo
    for job_url in job_urls:
        # Navegar a la URL del trabajo

        # Hacer clic en el botón para mostrar el equipo
        teams_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "teams-filter-acc"))
        )
        teams_button.click()

        # Esperar a que los elementos del equipo estén visibles
        try:
            time.sleep(1)  # Esperar un momento para permitir que el contenido se cargue

            title = driver.find_element(By.CSS_SELECTOR, "span.filters-list__title").text.strip()
            print(f"Title: {title}")
        except Exception as e:
            print("Title no encontrado")

        try:
            team = driver.find_element(By.CSS_SELECTOR, "span.teams-filter-checklst").text.strip()
            print(f"Team: {team}")
        except Exception as e:
            print("Team no encontrado")
        driver.get(job_url)

        # Esperar un poco para que se cargue la página completa
        time.sleep(3)

        # Imprimir los datos solicitados
        try:
            # Job Category
            job_category = driver.find_element(By.ID, "job-team-name").text.strip()
            print(f"Job Category: {job_category}")

            # Job Title
            job_title = driver.find_element(By.ID, "jdPostingTitle").text.strip()
            print(f"Job Title: {job_title}")

            # Job Location
            job_location = driver.find_element(By.ID, "job-location-name").text.strip()
            print(f"Job Location: {job_location}")

            # Posted Date
            posted_date = driver.find_element(By.ID, "jobPostDate").get_attribute('datetime').strip()
            print(f"Posted Date: {posted_date}")

            # Role Number
            role_number = driver.find_element(By.ID, "jobNumber").text.strip()
            print(f"Role Number: {role_number}")

            # Summary
            summary = driver.find_element(By.ID, "jd-job-summary").text.strip()
            print(f"Summary: {summary}")

            # Description
            description = driver.find_element(By.ID, "jd-description").text.strip()
            print(f"Description: {description}")

        except Exception as e:
            print(f"Error al obtener la información: {e}")

        # Imprimir la URL del trabajo
        print(f"Job URL: {job_url}")
        print("---------------------------------------------------")

        # Regresar a la página anterior
        driver.back()
        # Esperar a que la página anterior vuelva a cargar
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.arrow.arrow--blue.arrow--14"))
        )

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    # Cerrar el driver
    driver.quit()

