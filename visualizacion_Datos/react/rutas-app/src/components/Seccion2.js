import React from "react";

function Seccion2({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos
  const horas = Math.floor(datos[datos.length - 1]["distancia_total"] / 60);
  const minutos = Math.floor(datos[datos.length - 1]["distancia_total"] % 60);

  return (
    <div>
      <h2 style={styles.titulo}>Resumen de Rutas</h2>
      <div className="ruta-container">
        <p>Total de rutas generadas: {datos.length}</p>
        <p>
          Distancia total recorrida:{" "}
          {parseFloat(datos[datos.length - 1]["distancia_total"]).toFixed(2)} km
        </p>
        <p>
          Coste total:{" "}
          {parseFloat(datos[datos.length - 1]["coste_total"]).toFixed(2)} €
        </p>
        <p>
          Tiempo de ruta: {horas.toFixed(0)} h {minutos.toFixed(0)} min
        </p>
        <p>
          Tiempo de ejecucion:{" "}
          {parseFloat(datos[datos.length - 1]["tiempo_ejecucion"]).toFixed(2)} s
          por iteración
        </p>
      </div>
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

export default Seccion2;
