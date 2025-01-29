import sys
import os
from flask import Flask, jsonify
from flask_cors import CORS

# Obtener la ruta base del directorio actual (donde está server.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta a la carpeta que contiene el módulo
ruta_algoritmos = os.path.join(base_dir, '..', 'algoritmos', 'caso1')

# Agregar la ruta al sys.path
sys.path.append(ruta_algoritmos)

# Función para retrasar el import


def cargar_algoritmo():
    from algoritmo_genetico_caso1 import genetic_algorithm_multiple_runs
    return genetic_algorithm_multiple_runs()


# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Ejecutar el algoritmo genético y almacenar los resultados
ruta = cargar_algoritmo()

# Ruta API para obtener los datos en formato JSON


@app.route('/api/rutas', methods=['GET'])
def obtener_rutas():
    return jsonify(ruta)


# Ejecutar la aplicación Flask
if __name__ == "__main__":
    app.run(debug=False)
