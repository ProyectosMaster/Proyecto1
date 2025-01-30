import React from "react";

function Seccion1({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos

  return (
    <div style={styles.contenedor}>
      <h2 style={styles.titulo}>Resultados de las Rutas Generadas</h2>
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
          {/* <p>
            <strong>Costes totales:</strong> {ruta.coste_total}
          </p>
          <p>
            <strong>Distancia total:</strong> {ruta.distancia_total}
          </p> */}
        </div>
      ))}
    </div>
  );
}

// Estilos concretos
const styles = {
  contenedor: {
    padding: "20px",
    border: "1px solid #eee",
    borderRadius: "10px",
    backgroundColor: "#fafafa",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
  },
  titulo: {
    textAlign: "center", // Centrar el título
    color: "#007bff", // Color azul para el título
    marginBottom: "15px", // Espacio debajo del título
  },
};

export default Seccion1;
