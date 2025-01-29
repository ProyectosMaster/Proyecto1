import React from "react";

function BotonGenerar({ onGenerarDatos }) {
  return (
    <div>
      <button onClick={onGenerarDatos}>Generar Datos</button>
    </div>
  );
}

export default BotonGenerar;
