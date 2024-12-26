import numpy as np
import random

# Configuración de parámetros
NUM_GENERATIONS = 100
POPULATION_SIZE = 50
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.8

# Matriz de distancias (datos iniciales reales)
matriz_distancias = np.array([
    [0, 7.5625, 15.5365, 1.1998, 4.7145, 3.6614],
    [7.5625, 0, 3.3838, 7.7433, 14.572, 10.7361],
    [15.5365, 3.3838, 0, 12.5438, 0, 13.9021],
    [1.1998, 7.7433, 12.5438, 0, 5.0721, 3.3673],
    [4.7145, 14.572, 0, 5.0721, 0, 4.5417],
    [3.6614, 10.7361, 13.9021, 3.3673, 4.5417, 0]
])

# Vehículos disponibles
vehiculos = [
    {"id": 1, "capacidad": 2026, "costo_km": 0.2, "autonomia": 603},
    {"id": 2, "capacidad": 4362, "costo_km": 0.14, "autonomia": 630},
    {"id": 3, "capacidad": 4881, "costo_km": 0.2, "autonomia": 664},
    {"id": 4, "capacidad": 3321, "costo_km": 0.19, "autonomia": 514},
    {"id": 5, "capacidad": 10000, "costo_km": 0.32, "autonomia": 350},
    {"id": 6, "capacidad": 3129, "costo_km": 0.14, "autonomia": 791}
]

# Demandas de los clientes (incluye almacén como índice 0)
demands = [0, 909, 959, 960, 980, 979]

# Capacidad de vehículos
vehicle_capacities = [v["capacidad"] for v in vehiculos]

# Número de vehículos
num_vehicles = len(vehicle_capacities)

# Número de clientes
num_clients = len(demands) - 1

def fitness_function(routes):
    total_distance = 0
    for route in routes:
        if len(route) == 0:
            continue
        distance = 0
        prev_location = 0  # Comienza en el almacén
        for client in route:
            distance += matriz_distancias[prev_location][client]
            prev_location = client
        distance += matriz_distancias[prev_location][0]  # Regresa al almacén
        total_distance += distance
    return total_distance

def generate_initial_population():
    population = []
    clients = list(range(1, num_clients + 1))
    for _ in range(POPULATION_SIZE):
        random.shuffle(clients)
        population.append(split_routes(clients))
    return population

def split_routes(clients):
    routes = []
    current_route = []
    current_capacity = 0
    for client in clients:
        demand = demands[client]
        if current_capacity + demand <= vehicle_capacities[len(routes) % num_vehicles]:
            current_route.append(client)
            current_capacity += demand
        else:
            routes.append(current_route)
            current_route = [client]
            current_capacity = demand
    if current_route:
        routes.append(current_route)
    return routes

def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return parent1
    parent1_flat = [client for route in parent1 for client in route]
    parent2_flat = [client for route in parent2 for client in route]
    
    cut = random.randint(1, len(parent1_flat) - 1)
    child_flat = parent1_flat[:cut] + [c for c in parent2_flat if c not in parent1_flat[:cut]]
    return split_routes(child_flat)

def mutate(routes):
    if random.random() > MUTATION_RATE:
        return routes
    flat_list = [client for route in routes for client in route]
    random.shuffle(flat_list)
    return split_routes(flat_list)

def select_parents(population, fitnesses):
    idx = np.random.choice(len(population), size=2, replace=False, p=fitnesses / np.sum(fitnesses))
    return population[idx[0]], population[idx[1]]

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
    total_distance = fitness_function(best_solution)
    for i, route in enumerate(best_solution, start=1):
        print(f"Vehículo {i}: Ruta -> Almacén", end="")
        for client in route:
            print(f" -> Cliente {client}", end="")
        print(" -> Almacén")
    print(f"\nDistancia total recorrida: {total_distance:.2f} km")

if __name__ == "__main__":
    main()
