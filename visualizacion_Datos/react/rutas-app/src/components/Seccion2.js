import React from "react";

function Seccion2({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos

  return (
    <div style={styles.contenedor}>
      <h2 style={styles.titulo}>Resumen de Rutas</h2>
      <p>Total de rutas generadas: {datos.length}</p>
      <p>Distancia total recorrida: {datos[0]["distancia_total"]}</p>
      <p>Coste total: {datos[0]["coste_total"]}</p>
    </div>
  );
}

// Estilos concretos
const styles = {
  contenedor: {
    padding: "20px",
    border: "1px solid #eee",
    borderRadius: "10px",
    backgroundColor: "white",
    boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
  },
  titulo: {
    textAlign: "center", // Centrar el título
    color: "#007bff", // Color azul para el título
    marginBottom: "15px", // Espacio debajo del título
  },
};

export default Seccion2;
