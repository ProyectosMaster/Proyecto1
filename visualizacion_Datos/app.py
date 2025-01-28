from flask import Flask, jsonify
from algoritmoGenetico_caso1_bucle import genetic_algorithm_multiple_runs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Obtener la información de las rutas
ruta = genetic_algorithm_multiple_runs()


@app.route('/api/rutas', methods=['GET'])
def obtener_rutas():
    # Devolver las rutas en formato JSON
    return jsonify(ruta)


if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(debug=True)
