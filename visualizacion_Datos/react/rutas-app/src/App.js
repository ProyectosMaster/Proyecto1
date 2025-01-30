import React from "react";
import SeccionCaso from "./components/SeccionCaso";
import "./styles.css";
import Articulo1 from "./components/Articulo1";

function App() {
  // Array de casos para mapear dinámicamente
  const casos = ["caso1", "caso2", "caso3", "caso4"];

  return (
    <div>
      <h1>Aplicación de Rutas Grupo 1</h1>
      <Articulo1 />
      {casos.map((caso) => (
        <SeccionCaso key={caso} caso={caso} /> // Renderizar una sección por caso
      ))}
    </div>
  );
}

export default App;
