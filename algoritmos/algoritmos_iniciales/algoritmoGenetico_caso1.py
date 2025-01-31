import numpy as np
import random

# Configuración de parámetros
NUM_GENERATIONS = 700
POPULATION_SIZE = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.9

# Matriz de distancias (datos iniciales reales)
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

# Vehículos disponibles
vehiculos = [
    {"id": 1, "capacidad": 2026, "costo_km": 0.2, "autonomia": 603},
    {"id": 2, "capacidad": 4362, "costo_km": 0.14, "autonomia": 630},
    {"id": 3, "capacidad": 4881, "costo_km": 0.2, "autonomia": 664},
    {"id": 4, "capacidad": 3321, "costo_km": 0.19, "autonomia": 514},
    {"id": 5, "capacidad": 10000, "costo_km": 0.32, "autonomia": 350},
    {"id": 6, "capacidad": 3129, "costo_km": 0.14, "autonomia": 791},
]

# Demandas de los clientes (incluye almacén como índice 0)
demands = [
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
# Capacidad de vehículos
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
                return float("inf")  # Penalización severa
            distance += matriz_distancias[prev_location][client]
            prev_location = client
        distance += matriz_distancias[prev_location][20]
        total_distance += distance
    return total_distance


def generate_initial_population():
    population = []
    clients = list(range(0, 20))
    for _ in range(POPULATION_SIZE):
        random.shuffle(clients)
        route = split_routes(clients)
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


def info_ruta(route, vehicle):
    distancia = 0
    almacen = 20  # Comienza en el almacén
    demanda_total = 0
    id_vehiculo = 0

    for client in route:
        distancia += matriz_distancias[almacen][client]
        demanda_total += demands[client]
        almacen = client

    distancia += matriz_distancias[almacen][20]  # Regresa al almacén
    coste = distancia * vehicle["costo_km"]
    id_vehiculo = vehicle["id"]

    return distancia, demanda_total, coste, id_vehiculo


def genetic_algorithm():
    population = generate_initial_population()
    for generation in range(NUM_GENERATIONS):
        fitnesses = np.array([1 / (1 + fitness_function(ind)) for ind in population])
        new_population = []
        for _ in range(POPULATION_SIZE):
            parent1, parent2 = select_parents(population, fitnesses)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)
        population = new_population
        best_fitness = max(fitnesses)
        print(f"Generación {generation + 1}: Mejor aptitud: {best_fitness}")
    best_individual = population[np.argmax(fitnesses)]
    return best_individual


# Ejecutar el algoritmo
def main():
    best_solution = genetic_algorithm()
    print("\nMejor solución encontrada:")

    total_distance = 0
    total_cost = 0

    for i, route in enumerate(best_solution, start=1):
        vehicle = vehiculos[(i - 1) % len(vehiculos)]
        route_distance, route_demand, route_cost, id = info_ruta(route, vehicle)

        total_distance += route_distance
        total_cost += route_cost
        print(
            "------------------------------------------------------------------------------------"
        )
        print(f"Vehículo {id}: Ruta -> Almacén", end="")
        for client in route:
            print(f" -> Cliente {client+1}", end="")
        print(" -> Almacén")
        print(f"  Distancia recorrida: {route_distance:.2f} km")
        print(f"  Carga del vehículo: {route_demand} kg")
        print(f"  Costo de la ruta: ${route_cost:.2f}")

    print(f"\nDistancia total recorrida: {total_distance:.2f} km")
    print(f"Costo total: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
