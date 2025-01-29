import React from "react";

function Seccion2({ datos }) {
  if (!datos) return null; // No mostrar nada si no hay datos

  return (
    <div>
      <h2>Sección 2: Resumen de Rutas</h2>
      <p>Total de rutas generadas: {datos.length}</p>
    </div>
  );
}

export default Seccion2;
