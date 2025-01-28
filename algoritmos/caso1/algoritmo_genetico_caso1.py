import numpy as np
import pandas as pd
import random

# Configuración de parámetros
NUM_GENERATIONS = 700
POPULATION_SIZE = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.9

# Matriz de distancias (datos iniciales reales)
df_distancias = pd.read_excel("../datos/raw_data/df_distance_km.xlsx")
df_demandas = pd.read_excel("../datos/raw_data/df_historic_order_demand.xlsx")
df_demandas["order_demand"] = df_demandas["order_demand"].fillna(0)

matriz_distancias = df_distancias.values.tolist()
demandas_diciembre = df_demandas[df_demandas["mes_anio"] == "12-2024"]
demands = demandas_diciembre["order_demand"].tolist()

# Filtrar clientes con demanda mayor a 0
clientes_con_demanda = [i for i, demanda in enumerate(demands) if demanda > 0]

# Vehículos disponibles
vehiculos = [
    {"id": 1, "capacidad": 2026, "costo_km": 0.2, "autonomia": 603},
    {"id": 2, "capacidad": 4362, "costo_km": 0.14, "autonomia": 630},
    {"id": 3, "capacidad": 4881, "costo_km": 0.2, "autonomia": 664},
    {"id": 4, "capacidad": 3321, "costo_km": 0.19, "autonomia": 514},
    {"id": 5, "capacidad": 10000, "costo_km": 0.32, "autonomia": 350},
    {"id": 6, "capacidad": 3129, "costo_km": 0.14, "autonomia": 791},
]

# Ordenar los vehículos por costo por kilómetro (menor a mayor)
vehiculos = sorted(vehiculos, key=lambda v: v["costo_km"])
vehicle_capacities = [v["capacidad"] for v in vehiculos]

# Número de vehículos
num_vehicles = len(vehicle_capacities)


def fitness_function(routes):
    total_distance = 0
    for route in routes:
        if len(route) == 0:
            continue
        distance = 0
        prev_location = 20  # Comienza en el almacén
        for client in route:
            if matriz_distancias[prev_location][client] == 0:
                # Penalizar si no hay camino entre dos clientes
                return float("inf")  # Penalización
            distance += matriz_distancias[prev_location][client]
            prev_location = client
        distance += matriz_distancias[prev_location][20]
        total_distance += distance
    return total_distance


def generate_initial_population():
    population = []
    for _ in range(POPULATION_SIZE):
        random.shuffle(clientes_con_demanda)
        route = split_routes(clientes_con_demanda)
        if fitness_function(route) != float(
            "inf"
        ):  # Asegurarse de que sea una ruta válida
            population.append(route)
    return population


def split_routes(clients):
    routes = []
    current_route = []
    current_capacity = 0
    vehicle_index = 0

    for client in clients:
        demand = demands[client]
        # Asegurarse de que no exceda la capacidad del vehículo actual
        if current_capacity + demand <= vehicle_capacities[vehicle_index]:
            current_route.append(client)
            current_capacity += demand
        else:
            # Cambiar al siguiente vehículo si es necesario
            routes.append(current_route)
            current_route = [client]
            current_capacity = demand
            vehicle_index = (vehicle_index + 1) % num_vehicles
    if current_route:
        routes.append(current_route)
    return routes


def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1
    parent1_flat = [client for route in parent1 for client in route]
    parent2_flat = [client for route in parent2 for client in route]

    cut = random.randint(1, len(parent1_flat) - 1)
    child_flat = parent1_flat[:cut] + [
        c for c in parent2_flat if c not in parent1_flat[:cut]
    ]
    child = split_routes(child_flat)
    if fitness_function(child) == float("inf"):  # Verificar si la nueva ruta es válida
        return parent1  # Conservar el padre si el hijo no es válido
    return child


def mutate(routes):
    if random.random() > MUTATION_RATE:
        return routes
    flat_list = [client for route in routes for client in route]
    random.shuffle(flat_list)
    mutated = split_routes(flat_list)
    if fitness_function(mutated) == float("inf"):  # Verificar si la mutación es válida
        return routes  # Conservar la ruta original si la mutada no es válida
    return mutated


def select_parents(population, fitnesses):
    idx = np.random.choice(
        len(population), size=2, replace=False, p=fitnesses / np.sum(fitnesses)
    )
    return population[idx[0]], population[idx[1]]


def info_ruta(ruta, vehiculo):
    distancia = 0
    almacen = 20  # Comienza en el almacén
    demanda_total = 0
    id_vehiculo = 0

    for cliente in ruta:
        distancia += matriz_distancias[almacen][cliente]
        demanda_total += demands[cliente]
        almacen = cliente

    distancia += matriz_distancias[almacen][20]  # Regresa al almacén
    coste = distancia * vehiculo["costo_km"]
    id_vehiculo = vehiculo["id"]

    return round(distancia, 2), demanda_total, round(coste, 2), id_vehiculo


"""Al ser aleatorio el algoritmo genético, no me asegura que a la primera me encuentre un buena ruta por lo que
lo ejecuto 'x' veces y me quedo con el mejor resultado"""


def genetic_algorithm_multiple_runs(ejecuciones=5):
    mejor_solucion_global = None
    mejor_distancia_global = float("inf")
    info_mejor_ruta = None

    for ejecucion in range(ejecuciones):
        print(f"Ejecutando iteración {ejecucion + 1}/{ejecuciones}...")
        poblacion = generate_initial_population()

        for generation in range(NUM_GENERATIONS):
            fitnesses = np.array([1 / (1 + fitness_function(ind)) for ind in poblacion])
            nueva_poblacion = []
            for _ in range(POPULATION_SIZE):
                padre1, padre2 = select_parents(poblacion, fitnesses)
                hijo = crossover(padre1, padre2)
                hijo = mutate(hijo)
                nueva_poblacion.append(hijo)
            poblacion = nueva_poblacion

        # Evaluar la mejor solución de esta ejecución
        mejor_indice = np.argmax(fitnesses)
        mejor_solucion = poblacion[mejor_indice]
        distancia_actual = fitness_function(mejor_solucion)

        # Si es la mejor solución encontrada hasta ahora, guárdala (MIRAR NOMBRES)
        if distancia_actual < mejor_distancia_global:
            mejor_distancia_global = distancia_actual
            mejor_solucion_global = mejor_solucion

            # Generar detalles de las rutas
            info_mejor_ruta = []

            coste_total = 0
            for i, route in enumerate(mejor_solucion_global):
                ruta = ""
                vehicle = vehiculos[i % len(vehiculos)]
                distancia, demanda_total, coste, id_vehiculo = info_ruta(route, vehicle)
                coste_total += coste

                ruta += "Almacén"
                for client in route:
                    ruta += f" -> Cliente {client+1}"
                ruta += " -> Almacén"

                info_mejor_ruta.append(
                    {
                        "ruta": ruta,
                        "distancia": str(distancia).replace(".", ","),
                        "demanda_total": demanda_total,
                        "coste": str(coste).replace(".", ","),
                        "id_vehiculo": id_vehiculo,
                    }
                )

    # Imprimir resultados finales
    print("\nMejor solución encontrada:")
    for datos in info_mejor_ruta:
        capacidad_maxima_vehiculo = [
            v["capacidad"] for v in vehiculos if v["id"] == datos["id_vehiculo"]
        ]
        print(f"Vehículo {datos['id_vehiculo']}:")
        print(f"  Ruta: {datos['ruta']}")
        print(f"  Distancia recorrida: {datos['distancia']} km")
        print(
            f"  Demanda total: {datos['demanda_total']}/{capacidad_maxima_vehiculo}kg"
        )
        print(f"  Coste: {datos['coste']}€")

    print("-----------------------------------------------------------")
    mejor_distancia_global = round(mejor_distancia_global, 2)
    coste_total = round(coste_total, 2)
    print(
        f"Distancia total recorrida: {str(mejor_distancia_global).replace(".",",")} km"
    )
    print(f"Coste total de la ruta: {str(coste_total).replace(".",",")}€")


# Ejecutar el algoritmo genético múltiples veces
genetic_algorithm_multiple_runs()
