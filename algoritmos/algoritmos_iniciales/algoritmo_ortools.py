import pandas as pd
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
import os

path = "C:/Users/galla/Dropbox/PC/Documents/1 Pedro G Gallardo/Master IA y Big Data/Clases/octubre-24/2024-10-01/jupyter/Proyecto1/Datos_P1/"
os.chdir(path)


def create_data_model():
    data = {}

    # Cargar los datos desde el archivo Excel
    df = pd.read_excel(
        "df_distance_km.xlsx",
        index_col=0,
    )

    # Convertir los datos del DataFrame a una lista de listas para la matriz de distancias
    data["distance_matrix"] = df.values.tolist()

    # Debug: Imprimir la matriz de distancias
    print("Matriz de distancias:")
    print(data["distance_matrix"])

    # Actualizar data['demands'] con la columna 'order_demand' del archivo Excel
    df_demands = pd.read_excel("df_orders.xlsx")
    data["demands"] = df_demands["order_demand"].tolist()

    # Debug: Imprimir la lista de demandas
    print("Demandas:")
    print(data["demands"])

    # Actualizar data['vehicle_capacities'] con la columna 'vehicle_capacity' del archivo Excel
    df_vehicles = pd.read_excel("df_vehicle.xlsx")
    data["vehicle_capacities"] = df_vehicles[
        "capacidad_kg"
    ].tolist()  # Capacidades de los vehículos
    data["vehicle_autonomy"] = df_vehicles[
        "autonomia_km"
    ].tolist()  # Autonomías de los vehículos
    data["num_vehicles"] = len(df_vehicles["vehiculo_id"])  # Número de vehículos
    data["depot"] = 20  # Índice del almacén

    # Debug: Imprimir capacidades y autonomías de los vehículos, y número de vehículos
    print("Capacidades de los vehículos:")
    print(data["vehicle_capacities"])
    print("Autonomías de los vehículos:")
    print(data["vehicle_autonomy"])
    print("Número de vehículos:")
    print(data["num_vehicles"])

    return data


def main():
    data = create_data_model()
    manager = pywrapcp.RoutingIndexManager(
        len(data["distance_matrix"]), data["num_vehicles"], data["depot"]
    )
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        distance = data["distance_matrix"][from_node][to_node]
        if distance == 0 and from_node != to_node:
            return 999999  # Penalización alta para caminos inexistentes
        return distance

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    def demand_callback(from_index):
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index, 0, data["vehicle_capacities"], True, "Capacity"
    )

    # Añadir dimensión de autonomía
    routing.AddDimension(
        transit_callback_index,
        0,  # No slack
        max(data["vehicle_autonomy"]),  # Autonomía máxima de los vehículos
        True,  # Start cumulative to zero
        "Autonomy",
    )

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.seconds = 30  # Tiempo límite de búsqueda

    assignment = routing.SolveWithParameters(search_parameters)

    if assignment:
        print_solution(data, manager, routing, assignment)


def print_solution(data, manager, routing, assignment):
    total_distance = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = "Route for vehicle {}:\n".format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += " {} ->".format(manager.IndexToNode(index))
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id
            )
            print(
                routing.GetArcCostForVehicle(previous_index, index, vehicle_id),
                previous_index,
                index,
                vehicle_id,
            )
        plan_output += " {}\n".format(manager.IndexToNode(index))
        plan_output += "Distance of the route: {}km\n".format(route_distance)
        print(plan_output)
        total_distance += route_distance
    print("Total distance of all routes: {}km".format(total_distance))


if __name__ == "__main__":
    main()
