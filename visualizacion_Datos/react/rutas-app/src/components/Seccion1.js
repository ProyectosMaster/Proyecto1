import React from "react";

function Seccion1({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos

  return (
    <div>
      <h2 style={styles.titulo}>Resultados de las Rutas Generadas</h2>
      {datos.map((ruta, index) => (
        <div key={index} className="ruta-container">
          <h3>Ruta {index + 1}</h3>
          <ul>
            <li>
              <strong>Ruta:</strong> {ruta.ruta}
            </li>
            <li>
              <strong>Distancia:</strong>{" "}
              {parseFloat(ruta.distancia).toFixed(2)} km
            </li>
            <li>
              <strong>Demanda Total:</strong>{" "}
              {parseFloat(ruta.demanda_total).toFixed(2)} kg
            </li>
            <li>
              <strong>Coste:</strong> {parseFloat(ruta.coste).toFixed(2)} €
            </li>
            <li>
              <strong>ID Vehículo:</strong> {ruta.id_vehiculo}
              <ul>
                <li>
                  Autonomia: {parseFloat(ruta.capacidad_vehiculo).toFixed(2)} km
                </li>
                <li>
                  Capacidad: {parseFloat(ruta.autonomia_vehiculo).toFixed(2)} kg
                </li>
                <li>
                  Costo por km: {parseFloat(ruta.costo_km_vehiculo).toFixed(2)}{" "}
                  €
                </li>
              </ul>
            </li>
          </ul>
        </div>
      ))}
    </div>
  );
}

// Estilos concretos
const styles = {
  titulo: {
    textAlign: "center", // Centrar el título
    color: "#007bff", // Color azul para el título
    marginBottom: "15px", // Espacio debajo del título
  },
};

export default Seccion1;
