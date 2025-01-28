import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [rutas, setRutas] = useState([]);

  useEffect(() => {
    // Fetch de datos desde la API
    axios
      .get("http://127.0.0.1:5000/api/rutas")
      .then((response) => {
        setRutas(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener las rutas:", error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Resultados de las Rutas</h1>
      </header>
      <main>
        {rutas.map((ruta, index) => (
          <div key={index} className="ruta-container">
            <h2>Ruta {index + 1}</h2>
            <ul>
              <li>
                <strong>Ruta:</strong> {ruta.ruta}
              </li>
              <li>
                <strong>Distancia:</strong> {ruta.distancia}
              </li>
              <li>
                <strong>Demanda Total:</strong> {ruta.demanda_total}
              </li>
              <li>
                <strong>Coste:</strong> {ruta.coste}
              </li>
              <li>
                <strong>ID Vehículo:</strong> {ruta.id_vehiculo}
              </li>
            </ul>
            <p>
              <strong>Costes totales:</strong> {ruta.coste_total}
            </p>
            <p>
              <strong>Distancia total:</strong> {ruta.distancia_total}
            </p>
          </div>
        ))}
      </main>
    </div>
  );
}

export default App;
