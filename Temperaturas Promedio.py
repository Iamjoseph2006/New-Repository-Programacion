def calcular_temperatura_promedio(datos_ciudades):
    """
    Calcula la temperatura promedio de cada ciudad en un período de tiempo.

    Args:
        datos_ciudades (dict): Un diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas de temperaturas.

    Returns:
        dict: Un diccionario donde las claves son los nombres de las ciudades
              y los valores son las temperaturas promedio.
    """
    temperaturas_promedio = {}

    for ciudad, temperaturas in datos_ciudades.items():
        temperatura_promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio[ciudad] = temperatura_promedio

    return temperaturas_promedio

# Ejemplo de uso:
datos_ciudades = {
    'Shushufindi': [25, 26, 24, 23],
    'Lago Agrio': [28, 27, 26, 25]
}

temperaturas_promedio = calcular_temperatura_promedio(datos_ciudades)
print("Temperaturas Promedio:")
for ciudad, temperatura in temperaturas_promedio.items():
    print(f"{ciudad}: {temperatura}°C")
