# Scraping de Ofertas Laborales en Apple

Este proyecto utiliza Selenium para extraer datos de ofertas laborales de la página de carreras de Apple. El script navega por la web, accede a las ofertas de trabajo de la categoria "software and services", y recoge información relevante que luego se guarda en un archivo JSON.
## Requisitos

Asegúrate de tener lo siguiente instalado en tu entorno:

- Python 3.x
- Selenium
- ChromeDriver (asegúrate de que la versión sea compatible con tu versión de Chrome)

## Instalación

1. Clona este repositorio:

       git clone <URL_DEL_REPOSITORIO>
       cd <NOMBRE_DEL_REPOSITORIO>
2. Crea un entorno virtual (opcional pero recomendado):

        python -m venv venv
        source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
3. Instala las dependencias:

       pip install selenium
4. Descarga el controlador de navegador adecuado:

- Chrome: **ChromeDriver**

Asegúrate de que el controlador esté en tu PATH.

## Uso

1. Abre el script principal main.py y revisa el código si es necesario. 
2. Ejecuta el script:

       ```bash
       python main.py
3. Selecciona el navegador que deseas usar (Chrome o Firefox) cuando se te solicite.

## Funcionalidad

- Acceso a la página de carreras de Apple.
- Navegación a la sección de trabajos de Software y Servicios.
- Extracción de información relevante sobre cada oferta laboral, incluyendo:

  - Título del trabajo
  - Equipo asignado
  - Categoría del trabajo
  - Ubicación
  - Fecha de publicación
  - Número de rol
  - Resumen y descripción
  - Calificaciones clave o calificaciones preferidas
  - Rango salarial (mínimo y máximo)
- Almacenamiento de la información en un archivo JSON llamado trabajos.json.


## Ejemplo de Salida

El archivo trabajos.json tendrá la siguiente estructura para cada trabajo:

        [
            {
                "Title": "Software and Services:",
                "Team": "Apps and Frameworks",
                "Job Category": "Software and Services",
                "Job Title": "Python Software Development Engineer - Apps Services",
                "Job Location": "Cupertino, California, United States",
                "Posted Date": "20240924",
                "Role Number": "200569639",
                "Summary": "Imagine what you could do here. At Apple, great ideas have a way of becoming great products, services, and customer experiences very quickly. Bring passion and dedication to your job and there's no telling what you could accomplish. \n\nOur team runs the CI/CD pipeline for Apple's applications which supports thousands of developers around the globe. We are passionate about continuously improving the way we enable the software development lifecycle and push the envelope to reimagine cutting edge solutions to engineering problems of scale. As a member of the team, you would develop applications and micro-services to build and improve our next generation CI/CD pipeline.",
                "Description": "Develop and maintain CI/CD pipeline, services and integrations for Application development teams.\n\nCollaborate across teams to improve build, integration & release process.\n\nDevelop and maintain services and integrations for Apps Services CI/CD pipeline.\n\nMaintain and administrate dynamic Linux/macOS build farm.",
                "Key Qualifications": "B.S. in Computer Science or equivalent.\nProficient in Python programming.\nExperience with software development processes such as compilation, unit testing, code analysis, release process, and code coverage.\nExperience working on Linux and macOS based platforms.\nExperience with DevOps tools such as Ansible, Docker, Kubernetes.\nExperience with CI/CD process and platforms.\nAbility to participate in an after hours on-call rotation schedule.\nStrong analytical and problem solving skills.\nExcellent written and oral communication skills and ability to work with large development teams.",
                "Salario M\u00ednimo": 143100,
                "Salario M\u00e1ximo": 264200,
                "Job URL": "https://jobs.apple.com/en-us/details/200569639/python-software-development-engineer-apps-services?team=SFTWR"
            }
        ]


## Notas

- Asegúrate de que el sitio web de Apple esté disponible al momento de ejecutar el script.
- El tiempo de espera puede ser ajustado en el código según sea necesario para asegurar que todos los elementos se carguen correctamente.

## Contribuciones

Si deseas contribuir, siéntete libre de hacer un fork del repositorio y enviar un pull request.


