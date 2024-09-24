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

# Esperar a que se carguen los tbody
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.accordion-trigger")))

buttons = driver.find_elements(By.CSS_SELECTOR, "button.accordion-trigger")

for button in buttons:
    section_id = button.get_attribute('data-section-id')  # Obtener el id de la sección
    print(f"Haciendo clic en el botón de la sección: {section_id}")

    # Hacer clic en el botón
    button.click()

    # Esperar a que se cargue el contenido del acordeón
    time.sleep(1)  # Ajusta el tiempo según sea necesario

    # Buscar los elementos de interés:
    # 1. Obtener el "Team"
    try:
        team = driver.find_element(By.CSS_SELECTOR, f'span.filters-list__title').text.strip()
        print(f"Team: {team}")
    except:
        print("Team no encontrado")

    # 2. Obtener la "Category"
    try:
        category = driver.find_element(By.CSS_SELECTOR, f'span.teams-filter-checklst').text.strip()
        print(f"Category: {category}")
    except:
        print("Category no encontrada")

    # 3. Obtener la "Team Description"
    try:
        description = driver.find_element(By.CSS_SELECTOR, f'p#role_description_{section_id}').text.strip()
        print(f"Team Description: {description}")
    except:
        print("Descripción no encontrada")

    # 4. Obtener el link "Submit Resume"
    try:
        submit_link = driver.find_element(By.CSS_SELECTOR, f'a.btn.btn--md.btn--blue-gradient').get_attribute('href')
        print(f"Submit Resume link: {submit_link}")
    except:
        print("Link de Submit Resume no encontrado")

    # 5. Obtener el link "See full role description"
    try:
        full_role_description_link = driver.find_element(By.CSS_SELECTOR, f"a#role-description_{section_id}").get_attribute('href')
    # Acceder directamente a la página de "See full role description"
        driver.get(full_role_description_link)

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

    # 6. Obtener el enlace "Back to search results" y hacer clic para regresar
        try:
            back_to_search_link = driver.find_element(By.CSS_SELECTOR, "a.arrow.arrow--blue.arrow--left").get_attribute(
            'href')
        # Volver a la página de resultados de búsqueda
            driver.get(back_to_search_link)
        # Esperar para asegurar que la página se haya cargado
            time.sleep(2)

        except Exception as e:
            print(f"Link de 'Back to search results' no encontrado. Error: {e}")

    except Exception as e:
        print(f"Link de 'See full role description' no encontrado. Error: {e}")

# < a href = "/careers/us/hardware.html" class ="more" > Hardware < / a >

