# Archivos [Python]
# Ejemplos de clase

# Autor: Inove Coding School
# Version: 2.2

import csv


def altura_promedio(genero):
    print("¡Ejemplo integrador!")
    # Esta función recibe el género del cual
    # se debe calcular la altura promedio
    # puede ser --> femenino o masculino

    # Utilizar el archivo CSV "alturas",
    # el cual posee dos columnas:
    # - genero
    # - altura

    # Profe:
    # - Leer el archivo CSV
    with open('alturas.csv') as csvfile:
        datos_altura = list(csv.DictReader(csvfile))
        
    # - Recorrer todas las filas del archivo CSV
    # - En cada iteración obtenga la altura del genero objetivo

    lista_alturas = []

    for i in range(len(datos_altura)):
        if genero == datos_altura[i]['genero']:
            altura = float(datos_altura[i]['altura'])
            lista_alturas.append(altura)

    promedio = sum(lista_alturas) / len(lista_alturas)
    print(f'el promedio de la altura del genero {genero} es de: {promedio:.2f}')

    # - Acumule el valor y la cantidad para realizar
    #   el promedio al terminar el bucle

    sumatoria_altura = 0
    cantidad_altura = 0

    for i in range(len(datos_altura)):
        if genero == datos_altura[i]['genero']:
            altura = float(datos_altura[i]['altura'])
            sumatoria_altura += altura
            cantidad_altura += 1

    promedio = sumatoria_altura / cantidad_altura
    print(f'el promedio con sumatoria de la altura del genero {genero} es de: {promedio:.2f}')


    # --- Comience aquí a desarrollar su código ---


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    altura_promedio("femenino")
