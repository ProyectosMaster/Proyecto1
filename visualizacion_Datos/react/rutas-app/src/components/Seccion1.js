import React from "react";

function Seccion1({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos

  return (
    <div>
      <h2>Sección 1: Resultados de las Rutas</h2>
      {datos.map((ruta, index) => (
        <div key={index} className="ruta-container">
          <h3>Ruta {index + 1}</h3>
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
    </div>
  );
}

export default Seccion1;
