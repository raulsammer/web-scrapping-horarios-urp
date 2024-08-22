# Sistema para la Obtención de Información de Horarios Académicos usando Web Scraping

## Descripción del Proyecto
Este proyecto es una herramienta desarrollada para extraer de manera automatizada los datos de horarios académicos publicados en la [página web oficial de la Universidad Ricardo Palma](https://webapp.urp.edu.pe/guia-matricula/horario). Esta herramienta facilita la recopilación y transformación de estos datos en un formato estructurado (JSON), esencial para el funcionamiento del proyecto de [generador de horarios académicos](https://github.com/raulsammer/Generador-de-Horarios).

## Propósito del Proyecto
El propósito de este proyecto es permitir la extracción eficiente de datos de horarios académicos, que son fundamentales para herramientas de planificación académica. Surge de la necesidad de contar con los datos que la universidad publica en su [web](https://webapp.urp.edu.pe/guia-matricula/horario), y de la dificultad de obtenerlos manualmente o de manera directa desde la universidad.

## Filosofía y Lógica del Proyecto
La filosofía detrás de este proyecto radica en la automatización y en la necesidad de tener acceso a datos precisos y actualizados para el desarrollo de herramientas que beneficien a los estudiantes. Al no recibir fácilmente los datos necesarios de la universidad, y para poner en práctica mis conocimientos de web scraping, decidí crear este sistema como una solución efectiva para obtener esta información.

## Cómo Puede Ayudar
Este proyecto es esencial para estudiantes y desarrolladores que necesiten acceder a los datos de horarios académicos de la URP. Facilita la generación de archivos JSON, que pueden ser utilizados en aplicaciones de planificación de horarios, como el [generador de horarios académicos](https://github.com/raulsammer/Generador-de-Horarios), evitando la recolección manual y mejorando la eficiencia en la preparación de los horarios académicos.

## Características Principales
- **Automatización Completa**: Extrae datos de horarios automáticamente desde la [web oficial de la URP](https://webapp.urp.edu.pe/guia-matricula/horario).
- **Salida en Formato JSON**: Convierte la información extraída en un archivo JSON estructurado y listo para ser utilizado.
- **Compatibilidad Multi-Ciclo**: Soporta la extracción de datos para diversas carreras y ciclos académicos.
- **Interacción con Web Dinámica**: Maneja sitios web con contenido dinámico mediante técnicas avanzadas de web scraping.

## Cómo Usarlo
1. **Configuración Inicial**: Asegúrate de tener Python y las librerías necesarias instaladas (Selenium, Pandas, etc.).
2. **Ejecución del Script**: Ejecuta el script `main.py`, que abrirá un navegador y navegará automáticamente a la [página de horarios de la URP](https://webapp.urp.edu.pe/guia-matricula/horario).
3. **Selección de Opciones**: El script seleccionará automáticamente las opciones de carrera, malla curricular y semestre.
4. **Extracción y Almacenamiento**: Los horarios se extraen y se guardan en un archivo CSV, que luego se convierte a JSON usando `csv-to-json.py`.
5. **Integración**: Utiliza el archivo JSON generado en cualquier herramienta de planificación de horarios académicos, como el [generador de horarios](https://github.com/raulsammer/Generador-de-Horarios).

Este proyecto es **Open Source** y está diseñado para optimizar el proceso de obtención de datos para aplicaciones de planificación de horarios en la URP. 
