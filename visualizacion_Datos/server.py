import sys
import os
from flask import Flask, jsonify
from flask_cors import CORS

# Obtener la ruta base del directorio actual (donde está server.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar las rutas de los algoritmos a sys.path
for i in range(1, 5):
    caso = f"caso{i}"
    ruta_algoritmos = os.path.join(base_dir, '..', 'algoritmos', caso)
    sys.path.append(ruta_algoritmos)

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas


# Funciones para cargar los algoritmos
def cargar_caso1():
    from algoritmo_genetico_caso1 import genetic_algorithm_multiple_runs
    return genetic_algorithm_multiple_runs()


def cargar_caso2():
    from algoritmo_genetico_caso2 import genetic_algorithm_multiple_runs
    return genetic_algorithm_multiple_runs()


def cargar_caso3():
    from algoritmo_genetico_caso3 import genetic_algorithm_multiple_runs
    return genetic_algorithm_multiple_runs()


def cargar_caso4():
    from algoritmo_genetico_caso4 import genetic_algorithm_multiple_runs
    return genetic_algorithm_multiple_runs()


# Ejecutar el algoritmo genético y almacenar los resultados
caso1 = cargar_caso1()
caso2 = cargar_caso2()
caso3 = cargar_caso3()
caso4 = cargar_caso4()

# Ruta API para obtener los datos en formato JSON


@app.route('/api/caso1', methods=['GET'])
def obtener_caso1():
    return jsonify(caso1)


@app.route('/api/caso2', methods=['GET'])
def obtener_caso2():
    return jsonify(caso2)


@app.route('/api/caso3', methods=['GET'])
def obtener_caso3():
    return jsonify(caso3)


@app.route('/api/caso4', methods=['GET'])
def obtener_caso4():
    return jsonify(caso4)


# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=False)
