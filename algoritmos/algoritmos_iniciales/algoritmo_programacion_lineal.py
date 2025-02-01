import numpy as np
import pulp as lp

# Matriz de distancias y datos iniciales
matriz_distancias = np.array(
    [
        [
            0.0,
            7.5625,
            15.5365,
            1.1998,
            4.7145,
            1.7407,
            7.9408,
            17.1947,
            4.2933,
            3.2659,
            2.1866,
            6.0225,
            5.447,
            2.2133,
            11.1505,
            1.5775,
            10.8288,
            9.1456,
            20.4871,
            22.1445,
            3.6114,
        ],
        [
            7.5625,
            0.0,
            3.3838,
            7.743300000000001,
            14.572,
            8.523700000000002,
            0.4847,
            13.7974,
            10.1522,
            7.152100000000001,
            14.8113,
            10.1049,
            2.6961,
            13.4907,
            18.0835,
            7.0275,
            19.8218,
            8.273700000000002,
            9.636899999999999,
            19.1038,
            10.7361,
        ],
        [
            15.5365,
            3.3838,
            0.0,
            12.5438,
            0.0,
            0.0,
            0.0,
            16.0355,
            13.912,
            13.0649,
            17.0494,
            12.343,
            5.0114,
            15.7289,
            17.9217,
            9.6824,
            22.0599,
            10.5118,
            7.7574,
            16.5997,
            13.9021,
        ],
        [
            1.1998,
            7.743300000000001,
            12.5438,
            0.0,
            5.072100000000001,
            0.9118999999999999,
            7.579800000000001,
            17.4095,
            3.5781,
            3.3451,
            2.8532,
            6.233,
            4.7117,
            2.8799,
            11.361,
            1.3127,
            11.1926,
            9.3561,
            20.7019,
            21.1518,
            3.3673,
        ],
        [
            4.7145,
            14.572,
            0.0,
            5.072100000000001,
            0.0,
            4.8187,
            0.0,
            0.0,
            0.0,
            7.217,
            2.6253,
            6.8738,
            9.106399999999999,
            3.6476,
            12.0019,
            5.434699999999999,
            5.287199999999999,
            9.9969,
            21.3384,
            25.5947,
            4.5417,
        ],
        [
            1.7407,
            8.523700000000002,
            0.0,
            0.9118999999999999,
            4.8187,
            0.0,
            7.8866,
            20.0472,
            2.906,
            4.0899,
            2.889,
            8.875,
            5.0185,
            3.2185,
            14.003,
            2.0575,
            11.4008,
            11.9981,
            19.7467,
            20.4797,
            2.6952,
        ],
        [
            7.9408,
            0.4847,
            0.0,
            7.579800000000001,
            0.0,
            7.8866,
            0.0,
            13.9893,
            10.1499,
            7.344,
            15.0032,
            10.2968,
            0.0,
            0.0,
            0.0,
            7.219399999999999,
            20.0138,
            8.4656,
            9.828899999999999,
            17.1722,
            10.928,
        ],
        [
            17.1947,
            13.7974,
            16.0355,
            17.4095,
            0.0,
            20.0472,
            13.9893,
            0.0,
            19.6963,
            12.9161,
            16.1829,
            12.3127,
            13.5906,
            14.8623,
            5.9742,
            14.6038,
            22.6587,
            8.9984,
            15.5515,
            34.1368,
            20.8703,
        ],
        [
            4.2933,
            10.1522,
            13.912,
            3.5781,
            0.0,
            2.906,
            10.1499,
            19.6963,
            0.0,
            6.8679,
            3.5313,
            10.1024,
            7.722899999999999,
            4.5536,
            15.2304,
            4.8355,
            9.7565,
            13.2255,
            24.567,
            22.9781,
            1.0494,
        ],
        [
            3.2659,
            7.152100000000001,
            13.0649,
            3.3451,
            7.217,
            4.0899,
            7.344,
            12.9161,
            6.8679,
            0.0,
            4.7283,
            2.3061,
            4.9896,
            0.0,
            8.2196,
            0.0,
            10.8948,
            5.305,
            17.5604,
            21.1407,
            5.9516,
        ],
        [
            2.1866,
            14.8113,
            17.0494,
            2.8532,
            2.6253,
            2.889,
            15.0032,
            16.1829,
            3.5313,
            4.7283,
            0.0,
            6.5845,
            8.2105,
            1.6099,
            11.7126,
            3.397,
            7.7031,
            9.7077,
            21.0492,
            22.484,
            2.912,
        ],
        [
            6.0225,
            10.1049,
            12.343,
            6.233,
            6.8738,
            8.875,
            10.2968,
            12.3127,
            10.1024,
            2.3061,
            6.5845,
            0.0,
            6.4451,
            5.9051,
            5.6418,
            4.2199,
            12.2362,
            5.1248,
            16.4706,
            22.5962,
            10.2374,
        ],
        [
            5.447,
            2.6961,
            5.0114,
            4.7117,
            9.106399999999999,
            5.0185,
            0.0,
            13.5906,
            7.722899999999999,
            4.9896,
            8.2105,
            6.4451,
            0.0,
            10.0708,
            10.0675,
            4.2809,
            15.2069,
            6.286899999999999,
            12.4538,
            17.7187,
            7.9895,
        ],
        [
            2.2133,
            13.4907,
            15.7289,
            2.8799,
            3.6476,
            3.2185,
            0.0,
            14.8623,
            4.5536,
            0.0,
            1.6099,
            5.9051,
            10.0708,
            0.0,
            0.0,
            0.0,
            0.0,
            8.603299999999999,
            19.9448,
            23.8969,
            4.0306,
        ],
        [
            11.1505,
            18.0835,
            17.9217,
            11.361,
            12.0019,
            14.003,
            0.0,
            5.9742,
            15.2304,
            8.2196,
            11.7126,
            5.6418,
            10.0675,
            0.0,
            0.0,
            10.6147,
            21.7754,
            5.1865,
            18.4207,
            37.006,
            15.6084,
        ],
        [
            1.5775,
            7.0275,
            9.6824,
            1.3127,
            5.434699999999999,
            2.0575,
            7.219399999999999,
            14.6038,
            4.8355,
            0.0,
            3.397,
            4.2199,
            4.2809,
            0.0,
            10.6147,
            0.0,
            11.3728,
            8.927700000000002,
            20.2735,
            21.0351,
            4.155399999999999,
        ],
        [
            10.8288,
            19.8218,
            22.0599,
            11.1926,
            5.287199999999999,
            11.4008,
            20.0138,
            22.6587,
            9.7565,
            10.8948,
            7.7031,
            12.2362,
            15.2069,
            0.0,
            21.7754,
            11.3728,
            0.0,
            14.8006,
            26.1421,
            30.6412,
            8.5221,
        ],
        [
            9.1456,
            8.273700000000002,
            10.5118,
            9.3561,
            9.9969,
            11.9981,
            8.4656,
            8.9984,
            13.2255,
            5.305,
            9.7077,
            5.1248,
            6.286899999999999,
            8.603299999999999,
            5.1865,
            8.927700000000002,
            14.8006,
            0.0,
            14.7105,
            24.3734,
            13.2923,
        ],
        [
            20.4871,
            9.636899999999999,
            7.7574,
            20.7019,
            21.3384,
            19.7467,
            9.828899999999999,
            15.5515,
            24.567,
            17.5604,
            21.0492,
            16.4706,
            12.4538,
            19.9448,
            18.4207,
            20.2735,
            26.1421,
            14.7105,
            0.0,
            24.1215,
            22.0368,
        ],
        [
            22.1445,
            19.1038,
            16.5997,
            21.1518,
            25.5947,
            20.4797,
            17.1722,
            34.1368,
            22.9781,
            21.1407,
            22.484,
            22.5962,
            17.7187,
            23.8969,
            37.006,
            21.0351,
            30.6412,
            24.3734,
            24.1215,
            0.0,
            14.8282,
        ],
        [
            3.6114,
            10.7361,
            13.9021,
            3.3673,
            4.5417,
            2.6952,
            10.928,
            20.8703,
            1.0494,
            5.9516,
            2.912,
            10.2374,
            7.9895,
            4.0306,
            15.6084,
            4.155399999999999,
            8.5221,
            13.2923,
            22.0368,
            14.8282,
            0.0,
        ],
    ]
)

vehiculos = [
    {"id": 1, "capacidad": 2026, "costo_km": 0.2, "autonomia": 603},
    {"id": 2, "capacidad": 4362, "costo_km": 0.14, "autonomia": 630},
    {"id": 3, "capacidad": 4881, "costo_km": 0.2, "autonomia": 664},
    {"id": 4, "capacidad": 3321, "costo_km": 0.19, "autonomia": 514},
    {"id": 5, "capacidad": 10000, "costo_km": 0.32, "autonomia": 350},
    {"id": 6, "capacidad": 3129, "costo_km": 0.14, "autonomia": 791},
]

demandas = [
    909,
    959,
    960,
    980,
    979,
    908,
    924,
    920,
    886,
    964,
    942,
    974,
    950,
    932,
    938,
    891,
    968,
    972,
    901,
    881,
]

# Parámetros iniciales
num_clientes = len(demandas)
num_vehiculos = len(vehiculos)
almacen_idx = num_clientes

# Modelo de optimización
modelo = lp.LpProblem("Minimizar_Costo_Transporte", lp.LpMinimize)

# Variables de decisión: si un vehículo viaja entre i y j
x = lp.LpVariable.dicts(
    "ruta",
    [
        (i, j, v["id"])
        for i in range(num_clientes + 1)
        for j in range(num_clientes + 1)
        if i != j and matriz_distancias[i, j] > 0  # Excluir rutas con distancia 0
        for v in vehiculos
    ],
    cat=lp.LpBinary,
)

# Función objetivo: Minimizar el costo total
modelo += lp.lpSum(
    matriz_distancias[i, j] * x[(i, j, v["id"])] * v["costo_km"]
    for v in vehiculos
    for i in range(num_clientes + 1)
    for j in range(num_clientes + 1)
    if i != j and matriz_distancias[i, j] > 0
)

# Restricción: cada cliente debe ser visitado como mínimo una vez
for j in range(0, num_clientes + 1):
    modelo += (
        lp.lpSum(
            x[(i, j, v["id"])]
            for v in vehiculos
            for i in range(num_clientes + 1)
            if i != j and matriz_distancias[i, j] > 0
        )
        >= 1
    )

# Restricción: capacidad de los vehículos
for v in vehiculos:
    modelo += (
        lp.lpSum(
            demandas[j - 1]
            * lp.lpSum(
                x[(i, j, v["id"])]
                for i in range(num_clientes + 1)
                if i != j and matriz_distancias[i, j] > 0
            )
            for j in range(1, num_clientes + 1)
        )
        <= v["capacidad"]
    )

# Restricción: autonomía de los vehículos
for v in vehiculos:
    modelo += (
        lp.lpSum(
            matriz_distancias[i, j] * x[(i, j, v["id"])]
            for i in range(num_clientes + 1)
            for j in range(num_clientes + 1)
            if i != j and matriz_distancias[i, j] > 0
        )
        <= v["autonomia"]
    )

# Resolver el modelo
modelo.solve()

# Resultados del modelo
print("Estado del modelo:", lp.LpStatus[modelo.status])
print("Costo total:", lp.value(modelo.objective))


for v in vehiculos:
    ruta = []
    total_distancia_vehiculo = 0
    for i in range(num_clientes + 1):
        for j in range(num_clientes + 1):
            if (
                i != j
                and (i, j, v["id"]) in x
                and lp.value(x[(i, j, v["id"])])
                and matriz_distancias[i, j] > 0  # Asegurar que la distancia sea válida
            ):
                distancia = matriz_distancias[i, j]  # Obtener la distancia de la matriz
                if i not in ruta:  # Evitar duplicados en la ruta
                    ruta.append(i)
                if j not in ruta:
                    ruta.append(j)
                total_distancia_vehiculo += distancia  # Sumar la distancia

    if ruta:  # Solo imprimir si hay una ruta válida
        print(
            f"Ruta vehículo {v['id']}: 20{{{', '.join(map(str, ruta))}}}20, distancia recorrida = {total_distancia_vehiculo:.2f} km"
        )
