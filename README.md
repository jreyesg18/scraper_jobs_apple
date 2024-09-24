# Apple Careers Scraper

Este proyecto utiliza Selenium para hacer scraping de la página de carreras de Apple, extrayendo información sobre las ofertas de trabajo disponibles.

## Requisitos

Asegúrate de tener lo siguiente instalado en tu entorno:

- Python 3.x
- [Selenium](https://www.selenium.dev/)
- Controlador de navegador (ChromeDriver o GeckoDriver para Firefox)

## Instalación

1. Clona este repositorio:

       ```bash
       git clone <URL_DEL_REPOSITORIO>
       cd <NOMBRE_DEL_REPOSITORIO>
2. Crea un entorno virtual (opcional pero recomendado):

       ```bash
        python -m venv venv
        source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
3. Instala las dependencias:

       ```bash
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

## Cómo Funciona

El script realiza los siguientes pasos:

1. Accede a la página de carreras de Apple.
2. Navega a la sección de Software y Servicios.
3. Extrae información de las ofertas de trabajo, haciendo clic en los botones de acordeón para expandir cada sección.
4. Imprime la información extraída en la consola.

## Notas

- Asegúrate de que el sitio web de Apple esté disponible al momento de ejecutar el script.
- El tiempo de espera puede ser ajustado en el código según sea necesario para asegurar que todos los elementos se carguen correctamente.

## Contribuciones

Si deseas contribuir, siéntete libre de hacer un fork del repositorio y enviar un pull request.


