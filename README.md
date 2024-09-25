# Scraping de Ofertas Laborales en Apple

Este proyecto utiliza Selenium para extraer datos de ofertas laborales de la página de carreras de Apple. El script navega por la web, accede a las ofertas de trabajo, y recoge información relevante que luego se guarda en un archivo JSON.
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


## Notas

- Asegúrate de que el sitio web de Apple esté disponible al momento de ejecutar el script.
- El tiempo de espera puede ser ajustado en el código según sea necesario para asegurar que todos los elementos se carguen correctamente.

## Contribuciones

Si deseas contribuir, siéntete libre de hacer un fork del repositorio y enviar un pull request.


