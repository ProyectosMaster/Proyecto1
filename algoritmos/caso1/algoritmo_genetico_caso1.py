import numpy as np
import pandas as pd
import random
import os
import time

# Configuración de parámetros
NUM_GENERATIONS = 700
POPULATION_SIZE = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.9

# Configuración de rutas
base_dir = os.path.dirname(os.path.abspath(__file__))
distancias_path = os.path.join(
    base_dir, "..", "..", "datos", "raw_data", "df_distance_km.xlsx"
)
demandas_path = os.path.join(
    base_dir, "..", "..", "datos", "raw_data", "df_historic_order_demand.xlsx"
)

# Matriz de distancias (datos iniciales reales)
df_distancias = pd.read_excel(distancias_path)
df_demandas = pd.read_excel(demandas_path)
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
vehicle_autonomies = [v["autonomia"] for v in vehiculos]

# Número de vehículos
num_vehicles = len(vehicle_capacities)


def fitness_function(routes):
    """
    Evalua que tan buena es la solución midiendo la distancia total recorrida.
    Penaliza soluciones invalidas si:
    - La distancia entre clientes es 0
    - La ruta excede la autonomía del vehiculo
    """
    total_distance = 0
    for i, route in enumerate(routes):
        if len(route) == 0:
            continue
        distance = 0
        prev_location = 20  # Comienza en el almacén
        for client in route:
            if matriz_distancias[prev_location][client] == 0:
                return float("inf")
            distance += matriz_distancias[prev_location][client]
            prev_location = client
        distance += matriz_distancias[prev_location][20]

        if distance > vehicle_autonomies[i % num_vehicles]:
            return float("inf")

        total_distance += distance
    return total_distance


def generate_initial_population():
    """
    Genera una población de soluciones aleatorias mezclando los clientes con demanda y dividiendo
    las rutas.
    """
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
    """
    Divide una lista de clientes en rutas viables teniendo en cuenta:
    - Capacidad y autonomía del vehículo
    - Empezar y finalizaar las rutas en el almacén
    - Pasa al siguiente vehículo si supera alguna restricción
    """
    routes = []
    current_route = []
    current_capacity = 0
    current_distance = 0
    vehicle_index = 0
    prev_location = 20  # Almacén

    for client in clients:
        demand = demands[client]
        distance_to_client = matriz_distancias[prev_location][client]
        distance_return = matriz_distancias[client][20]

        if (
            current_capacity + demand <= vehicle_capacities[vehicle_index]
            and current_distance + distance_to_client + distance_return
            <= vehicle_autonomies[vehicle_index]
        ):
            current_route.append(client)
            current_capacity += demand
            current_distance += distance_to_client
            prev_location = client
        else:
            routes.append(current_route)
            current_route = [client]
            current_capacity = demand
            current_distance = matriz_distancias[20][client]
            prev_location = client
            vehicle_index = (vehicle_index + 1) % num_vehicles
    if current_route:
        routes.append(current_route)
    return routes


def crossover(parent1, parent2):
    """
    Cruza dos rutas para generar un hijo:
    - Selecciona una parte de un padre y la junta con las partes del otro padre que no coincidan.
    - Verifica que sea valida y si no, se mantiene la del primer padre.
    """
    if random.random() > CROSSOVER_RATE:
        return parent1
    parent1_flat = [client for route in parent1 for client in route]
    parent2_flat = [client for route in parent2 for client in route]

    cut = random.randint(1, len(parent1_flat) - 1)
    child_flat = parent1_flat[:cut] + [
        c for c in parent2_flat if c not in parent1_flat[:cut]
    ]
    child = split_routes(child_flat)
    # Verificar si la nueva ruta es válida
    if fitness_function(child) == float("inf"):
        return parent1  # Conservar el padre si el hijo no es válido
    return child


def mutate(routes):
    """
    Realiza una mutación aleatoria a una solución:
    - Mezcla los clientes de dicha solución y vuelve a generar una ruta con esa mezcla.
    - Se comprueba que sea válida.
    """
    if random.random() > MUTATION_RATE:
        return routes
    flat_list = [client for route in routes for client in route]
    random.shuffle(flat_list)
    mutated = split_routes(flat_list)
    # Verificar si la mutación es válida
    if fitness_function(mutated) == float("inf"):
        return routes  # Conservar la ruta original si la mutada no es válida
    return mutated


def select_parents(population, fitnesses):
    """
    Selecciona dos soluciones mediante el metodo de la ruleta para utilizarlas en la funcion crossover
    """
    idx = np.random.choice(
        len(population), size=2, replace=False, p=fitnesses / np.sum(fitnesses)
    )
    return population[idx[0]], population[idx[1]]


def info_ruta(ruta, vehiculo):
    """
    Calcula la información de una ruta específica.
    :param ruta: Lista de clientes en la ruta.
    :param vehiculo: Diccionario con la información del vehículo.
    :return: Tupla con (distancia, demanda_total, coste, id_vehiculo, capacidad, costo_km, autonomia)
    """
    distancia = 0
    almacen = 20  # Comienza en el almacén
    demanda_total = 0

    for cliente in ruta:
        distancia += matriz_distancias[almacen][cliente]
        demanda_total += demands[cliente]
        almacen = cliente

    distancia += matriz_distancias[almacen][20]  # Regresa al almacén
    coste = distancia * vehiculo["costo_km"]

    return (
        round(distancia, 2),
        demanda_total,
        round(coste, 2),
        vehiculo["id"],
        vehiculo["capacidad"],
        vehiculo["costo_km"],
        vehiculo["autonomia"],
    )


def genetic_algorithm_multiple_runs(ejecuciones=5):
    """
    Llama a todas las funciones anteriores y por cada ejecución se queda con la mejor solución(fitness)
    y compara con la anterior solución para quedarse con la que menor distancia recorra.
    """
    mejor_solucion_global = None
    mejor_distancia_global = float("inf")
    info_mejor_ruta = None

    for ejecucion in range(ejecuciones):
        print(f"Ejecutando iteración {ejecucion + 1}/{ejecuciones}...")
        start_time = time.time()  # Iniciar el contador de tiempo
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
        end_time = time.time()  # Finalizar el contador de tiempo

        # Si es la mejor solución encontrada hasta ahora, guárdala
        if distancia_actual < mejor_distancia_global:
            mejor_distancia_global = distancia_actual
            mejor_solucion_global = mejor_solucion

            # Generar detalles de las rutas
            info_mejor_ruta = []
            coste_total = 0

            for i, route in enumerate(mejor_solucion_global):
                vehicle = vehiculos[i % len(vehiculos)]
                (
                    distancia,
                    demanda_total,
                    coste,
                    id_vehiculo,
                    capacidad,
                    costo_km,
                    autonomia,
                ) = info_ruta(route, vehicle)

                coste_total += coste

                ruta_str = "Almacén"
                for client in route:
                    ruta_str += f" -> Cliente {client + 1}"
                ruta_str += " -> Almacén"

                info_mejor_ruta.append(
                    {
                        "ruta": ruta_str,
                        "distancia": distancia,
                        "demanda_total": demanda_total,
                        "coste": coste,
                        "id_vehiculo": id_vehiculo,
                        "capacidad_vehiculo": capacidad,
                        "costo_km_vehiculo": costo_km,
                        "autonomia_vehiculo": autonomia,
                        "coste_total": coste_total,
                        "distancia_total": mejor_distancia_global,
                        "tiempo_ejecucion": (end_time - start_time),
                    }
                )

    # Imprimir resultados finales
    print("\nMejor solución encontrada:")
    for datos in info_mejor_ruta:
        print(f"Vehículo {datos['id_vehiculo']}:")
        print(f"  Ruta: {datos['ruta']}")
        print(f"  Distancia recorrida: {datos['distancia']} km")
        print(
            f"  Demanda total: {
              datos['demanda_total']}/{datos['capacidad_vehiculo']} kg"
        )
        print(f"  Coste: {datos['coste']} €")
        print(f"  Costo por kilómetro: {datos['costo_km_vehiculo']} €/km")
        print(f"  Autonomía del vehículo: {datos['autonomia_vehiculo']} km")

    print("-----------------------------------------------------------")
    mejor_distancia_global = round(mejor_distancia_global, 2)
    coste_total = round(coste_total, 2)
    print(
        f"Distancia total recorrida: {
          str(mejor_distancia_global).replace(".", ",")} km"
    )
    print(f"Coste total de la ruta: {str(coste_total).replace(".", ",")} €")

    return info_mejor_ruta


# Ejecutar el algoritmo genético múltiples veces
genetic_algorithm_multiple_runs()
