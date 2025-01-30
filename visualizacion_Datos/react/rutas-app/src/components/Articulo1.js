import React from "react";
import MapComponent from "./MapComponent";

function Articulo1() {
  return (
    <div style={styles.contenedor}>
      <h2 style={styles.titulo}>Mapa real de los clientes</h2>
      <MapComponent />
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
    marginBottom: "30px",
  },
  titulo: {
    textAlign: "center", // Centrar el título
    color: "#007bff", // Color azul para el título
    marginBottom: "15px", // Espacio debajo del título
  },
};

export default Articulo1;
