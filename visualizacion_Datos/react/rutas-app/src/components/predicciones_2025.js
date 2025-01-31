import React, { useState, useEffect } from "react";
import Papa from "papaparse";
import "./CsvTable.css"; // Importar el archivo CSS

const CsvTable = () => {
  const [data, setData] = useState([]); // Estado para almacenar los datos del CSV
  const [headers, setHeaders] = useState([]); // Estado para almacenar los encabezados

  useEffect(() => {
    // Ruta al archivo CSV en la carpeta public
    const csvFilePath = "/pedidos_2025.csv";

    // Usar fetch para obtener el contenido del archivo CSV
    fetch(csvFilePath)
      .then((response) => response.text()) // Convertir la respuesta a texto
      .then((csvText) => {
        // Parsear el CSV usando PapaParse
        Papa.parse(csvText, {
          header: true, // Indicar que la primera fila son los encabezados
          dynamicTyping: true, // Convertir automáticamente los valores a tipos de datos correctos
          complete: (result) => {
            // Guardar los encabezados y los datos en el estado
            setHeaders(result.meta.fields);
            setData(result.data);
          },
          error: (error) => {
            console.error("Error al parsear el CSV:", error);
          },
        });
      })
      .catch((error) => {
        console.error("Error al cargar el archivo CSV:", error);
      });
  }, []); // El efecto se ejecuta solo una vez al montar el componente

  return (
    <div className="table-container">
      {data.length > 0 ? (
        <table className="table">
          <thead>
            <tr>
              {headers.map((header, index) => (
                <th key={index}>{header}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, rowIndex) => (
              <tr key={rowIndex}>
                {headers.map((header, colIndex) => (
                  <td key={colIndex}>{row[header]}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p className="loading-message">Cargando datos...</p>
      )}
    </div>
  );
};

export default CsvTable;
