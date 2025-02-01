import React from "react";

const MapComponent = () => {
  return (
    <div
      style={{
        width: "80%",
        height: "400px",
        display: "block",
        margin: "0 auto",
      }}
    >
      <iframe
        src="/mapa.html"
        width="100%"
        height="100%"
        style={{ border: "none" }}
        title="Mapa"
      ></iframe>
    </div>
  );
};

export default MapComponent;
