from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv
import time

options = webdriver.FirefoxOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Firefox(options=options)

driver.get("https://webapp.urp.edu.pe/guia-matricula/horario")

def wait_for_element_clickable(element_id, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.ID, element_id)))

def selectOptions():
    selCar = wait_for_element_clickable('txtCarrera')
    selectCar = Select(selCar)
    opciones = [option.text for option in selectCar.options[1:]]  # Excluir la primera opción
    return opciones

def seleCar():
    selCar = wait_for_element_clickable('txtCarrera')
    selectCar = Select(selCar)
    
    for option in selectCar.options[1:]:  # Comenzar desde la segunda opción
        selectCar.select_by_visible_text(option.text)
        time.sleep(1)  # Pequeña pausa para asegurar la carga de elementos dependientes
        seleCurri(selCar, selectCar)  # Pasar selCar y selectCar como argumentos

def seleCurri(selCar, selectCar):  # Aceptar selCar y selectCar como argumentos
    seleCurri = wait_for_element_clickable('txtCurricula')
    selectCurri = Select(seleCurri)
    for option in selectCurri.options[1:]:  # Comenzar desde la segunda opción
        if "50" not in option.text:
            selectCurri.select_by_visible_text(option.text)
            time.sleep(1)  # Esperar a que la página reaccione
            seleSemes(selCar, selectCar, selectCurri)  # Pasar selCar, selectCar y selectCurri

def seleSemes(selCar, selectCar, selectCurri):  # Aceptar selCar, selectCar y selectCurri
    seleSemes = wait_for_element_clickable('txtCiclo')
    selectSemes = Select(seleSemes)
    
    with open('tabla.csv', 'a', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        
        for option in selectSemes.options[1:]:
            selectSemes.select_by_visible_text(option.text)
            time.sleep(1)  # Esperar a que la página reaccione
            datos_tabla = extraer_datos_tabla()
            
            if datos_tabla and not archivo_csv.tell():  # Si el archivo está vacío, añade el encabezado
                encabezado = ['Carrera', 'Malla'] + extraer_encabezado_tabla()
                escritor_csv.writerow(encabezado)
                
            nombre_carrera = selectCar.first_selected_option.text
            nombre_malla = selectCurri.first_selected_option.text
            for fila in datos_tabla:
                fila.insert(0, nombre_malla)
                fila.insert(0, nombre_carrera)
                escritor_csv.writerow(fila)

def extraer_datos_tabla():
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="divContainer"]/div[2]/div/div/table')))
    tabla = driver.find_element(By.XPATH, '//*[@id="divContainer"]/div[2]/div/div/table')
    filas = tabla.find_elements(By.TAG_NAME, 'tr')
    datos_tabla = []
    
    for fila in filas[1:]:  # Excluir el encabezado
        celdas = fila.find_elements(By.TAG_NAME, 'td')
        datos_fila = [celda.text for celda in celdas]
        datos_tabla.append(datos_fila)
    
    return datos_tabla

def extraer_encabezado_tabla():
    tabla = driver.find_element(By.XPATH, '//*[@id="divContainer"]/div[2]/div/div/table')
    encabezado = tabla.find_elements(By.TAG_NAME, 'th')
    return [celda.text for celda in encabezado]

selectOptions()
seleCar()

driver.quit()
