import React, { useState } from "react";
import axios from "axios";
import BotonGenerar from "./BotonGenerar";
import Seccion1 from "./Seccion1";
import Seccion2 from "./Seccion2";

const SeccionCaso = ({ caso }) => {
  const [datos, setDatos] = useState(null); // Estado para almacenar los datos de la API
  const [mostrarDatos, setMostrarDatos] = useState(false); // Estado para controlar la visibilidad de los datos

  // Función para obtener los datos de la API
  const generarDatos = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/api/${caso}`);
      setDatos(response.data); // Almacenar los datos en el estado
      setMostrarDatos(true); // Mostrar los datos después de obtenerlos
    } catch (error) {
      console.error(`Error al obtener las rutas para ${caso}:`, error);
    }
  };

  return (
    <div className="ruta-container">
      <h2 style={styles.titulo}>{caso.toUpperCase()}</h2>{" "}
      {/* Título de la sección */}
      <BotonGenerar onGenerarDatos={generarDatos} />{" "}
      {/* Botón para generar datos */}
      {mostrarDatos &&
        datos && ( // Mostrar los datos solo si hay datos y mostrarDatos es true
          <div className="seccion-contenedor">
            <div className="seccion-izquierda">
              <Seccion1 datos={datos} />
            </div>
            <div className="seccion-derecha">
              <Seccion2 datos={datos} />
            </div>
          </div>
        )}
    </div>
  );
};

// Estilos concretos
const styles = {
  titulo: {
    textAlign: "center", // Centrar el título
    color: "#007bff", // Color azul para el título
    marginBottom: "15px", // Espacio debajo del título
  },
};

export default SeccionCaso;
