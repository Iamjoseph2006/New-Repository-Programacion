def calcular_promedio_temperaturas(ciudades_temperaturas):
    promedios_ciudades = []

    for ciudad_temperaturas in ciudades_temperaturas:
        suma_temperaturas = 0
        total_dias = 0

        for semana in ciudad_temperaturas:
            for dia in semana:
                suma_temperaturas += dia['temp']
                total_dias += 1

        promedio_ciudad = suma_temperaturas / total_dias
        promedios_ciudades.append(promedio_ciudad)

    return promedios_ciudades


# Datos de temperaturas de las ciudades
temperaturas = [
    [  # Shushufindi
        [  # Semana 1
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 29},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 25}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 27},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 24}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 31},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  # Lago Agrio
        [  # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 27}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 28}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ]
    ]
]

# Llamar a la función y mostrar resultados
ciudades_promedios = calcular_promedio_temperaturas(temperaturas)
ciudades = ["Shushufindi", "Lago Agrio"]

for i, ciudad in enumerate(ciudades):
    print(f"Temperatura promedio en {ciudad}: {ciudades_promedios[i]:.2f}°C")