from flask import Flask, render_template_string
from algoritmoGenetico_caso1_bucle import genetic_algorithm_multiple_runs
import json  # Para serializar los datos de ruta

app = Flask(__name__)

# Obtener la información de las rutas
ruta = genetic_algorithm_multiple_runs()


@app.route('/')
def mostrar_resultados():
    # Convertir la variable ruta en JSON para enviarla al navegador
    rutas_json = json.dumps(ruta)

    # Plantilla HTML para mostrar las rutas
    html_template = """
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Resultados de Rutas English</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; font-size: 18px; }
            strong { color: #007BFF; }
            .ruta-container { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Resultados de las Rutas</h1>
        <div id="resultados"></div>

        <script>
            // Datos de rutas serializados desde el servidor
            const rutas = {{ rutas_json | safe }};
            
            // Obtener el contenedor donde se mostrarán los resultados
            const resultados = document.getElementById('resultados');

            // Iterar sobre las rutas y mostrarlas
            rutas.forEach((ruta, index) => {
                const rutaHTML = `
                    <div class="ruta-container">
                        <h2>Ruta ${index + 1}</h2>
                        <ul>
                            <li><strong>Ruta:</strong> ${ruta.ruta}</li>
                            <li><strong>Distancia:</strong> ${ruta.distancia}</li>
                            <li><strong>Demanda Total:</strong> ${ruta.demanda_total}</li>
                            <li><strong>Coste:</strong> ${ruta.coste}</li>
                            <li><strong>ID Vehículo:</strong> ${ruta.id_vehiculo}</li>
                        </ul>
                        <p>Costes totales: <span id="coste_total">${ruta.coste_total}</span>
                        <p>Distancia total: <span id="distancia_total">${ruta.distancia_total}</span>
                    </div>
                `;
                resultados.innerHTML += rutaHTML;
            });
        </script>

    </body>
    </html>
    """
    # Renderizar la plantilla con los datos de rutas en formato JSON
    return render_template_string(html_template, rutas_json=rutas_json)


@app.route('/es')
def mostrar_resultados_es():
    # Convertir la variable ruta en JSON para enviarla al navegador
    rutas_json = json.dumps(ruta)

    # Plantilla HTML para mostrar las rutas
    html_template = """
    <!DOCTYPE html>
    <html lang='es'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Resultados de Rutas</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #333; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; font-size: 18px; }
            span { font-size: 18px; }
            strong { color: #007BFF; }
            .ruta-container { margin-bottom: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Resultados de las Rutas</h1>
        <div id="resultados"></div>

        <script>
            // Datos de rutas serializados desde el servidor
            const rutas = {{ rutas_json | safe }};
            
            // Obtener el contenedor donde se mostrarán los resultados
            const resultados = document.getElementById('resultados');

            // Iterar sobre las rutas y mostrarlas
            rutas.forEach((ruta, index) => {
                const rutaHTML = `
                    <div class="ruta-container">
                        <h2>Ruta ${index + 1}</h2>
                        <ul>
                            <li><strong>Ruta:</strong> ${ruta.ruta}</li>
                            <li><strong>Distancia:</strong> ${ruta.distancia}</li>
                            <li><strong>Demanda Total:</strong> ${ruta.demanda_total}</li>
                            <li><strong>Coste:</strong> ${ruta.coste}</li>
                            <li><strong>ID Vehículo:</strong> ${ruta.id_vehiculo}</li>
                        </ul>
                        <p><strong>Costes totales:</strong> <span>${ruta.coste_total}</span></p>
                        <p><strong>Distancia total:</strong> <span>${ruta.distancia_total}</span></p>
                    </div>
                `;
                resultados.innerHTML += rutaHTML;
            });
        </script>

    </body>
    </html>
    """
    # Renderizar la plantilla con los datos de rutas en formato JSON
    return render_template_string(html_template, rutas_json=rutas_json)


if __name__ == "__main__":
    # Ejecutar la aplicación Flask
    app.run(debug=True)
