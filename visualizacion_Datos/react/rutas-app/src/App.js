import React, { useState } from "react";
import axios from "axios";
import BotonGenerar from "./components/BotonGenerar";
import Seccion1 from "./components/Seccion1";
import Seccion2 from "./components/Seccion2";
import "./styles.css";

function App() {
  const [datos, setDatos] = useState(null); // Estado para almacenar los datos de la API

  // Función para obtener los datos de la API
  const generarDatos = async () => {
    try {
      const response = await axios.get("http://localhost:5000/api/rutas");
      setDatos(response.data); // Almacenar los datos en el estado
    } catch (error) {
      console.error("Error al obtener las rutas:", error);
    }
  };

  return (
    <div>
      <h1>Aplicación de Rutas</h1>
      <BotonGenerar onGenerarDatos={generarDatos} />
      {datos && ( // Mostrar las secciones solo si hay datos
        <>
          <Seccion1 datos={datos} />
          <Seccion2 datos={datos} />
        </>
      )}
    </div>
  );
}

export default App;
