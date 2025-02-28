﻿# P1_Mercancias_perecederas

1. Objetivos principales

- Minimizar coste total: Optimizar las rutas de entrega para reducir el coste total, teniendo en cuenta tanto el coste por kilómetro de cada vehículo como el uso eficiente de la capacidad de carga y la autonomía.
- Maximizar el número de pedidos entregados: Planificar las rutas para entregar el mayor número de pedidos posible dentro de las limitaciones de los recursos disponibles (vehículos, capacidad de carga, autonomía, etc.), maximizando la eficiencia operativa.

2. Restricciones

- Capacidad de carga de los vehículos: Cada vehículo tiene una capacidad máxima de carga en kilogramos que no debe excederse, por lo que los pedidos deben ser distribuidos eficientemente
  entre los vehículos disponibles.
- Autonomía limitada de los vehículos: Cada vehículo tiene una autonomía máxima en kilómetros. Las rutas deben ser ajustadas para que ningún vehículo supere su autonomía durante el día de
  operación.
- Considera que el vehículo puede necesitar retornar a su punto de inicio, por lo que la autonomía se debe planificar de forma adecuada.
- Todas las rutas empiezan y acaban en el almacén

3. Datos

- Tabla flota vehículos  df_vehicle
- Tabla localizaciones (almacén y clientes)  df_location
- Matriz distancias entre localizaciones en km  df_distance_km
- Matriz distancias entre localizaciones en tiempo  df_distance_min
- Tabla de pedidos  df_orders
- Histórico de pedidos  df_historic_order_demand

4. Estructura de carpetas

- Profiling:
  - Readme.md
  - df_distance_km.html
  - df_distance_min.html
  - df_historic_order_demand.html
  - df_location.html
  - df_orders.html
  - df_vehicle.html
- Algoritmos:
  - algoritmos_iniciales:
    - algoritmo_djikstra.ipynb
    - algoritmo_ortools.py
    - algoritmo_programacion_lineal.py
    - EDA.ipynb
  - caso 1:
    - \__pycache_:
      - algoritmo_genetico_caso1.cpython-312.pyc
    - README.md
    - algoritmo_genetico_caso1.py
  - caso 2:
    - \__pycache_:
      - algoritmo_genetico_caso2.cpython-312.pyc
    - README.md
    - algoritmo_genetico_caso2.py
  - caso 3:
    - \__pycache_:
      - algoritmo_genetico_caso3.cpython-312.pyc
    - README.md
    - algoritmo_genetico_caso3.py
  - caso 4:
    - \__pycache_:
      - algoritmo_genetico_caso4.cpython-312.pyc
    - README.md
    - algoritmo_genetico_caso4.py
  - README.md
- Datos:

  - map:
    - mapa.html
    - mapas.ipynb
  - prediccion:
    - pedidos_2025.csv
  - raw_data:
    - df_distance_km.xlsx
    - df_distance_min.xlsx
    - df_historic_order_demand.xlsx
    - df_location.xlsx
    - df_orders.xlsx
    - df_vehicle.xlsx

- Documentacion:

  - Documentacion.pdf
  - manual_de_usuario.pdf (se incluye arquitectura del sistema)

- Modelos:

  - README.md
  - predicciones_enero2025.ipynb

- video_web:

  - README.md
  - video_prototipo.mkv

- Visualizacion_Datos:

  - \__pycache_:
    - algoritmoGenetico_caso1_bucle.cpython-312.pyc
  - react:
    - rutas-app:
      - \__pycache_:
        - algoritmoGenetico_caso1_bucle.cpython-312.pyc
      - public:
        - favicon.ico
        - index.html
        - logo192.png
        - logo512.png
        - manifest.json
        - mapa.html
        - pedidos_2025.csv
        - robots.txt
      - src:
        - components:
          - Articulo1.js
          - BotonGenerar.js
          - CsvTable.css
          - MapComponent.js
          - Seccion1.js
          - Seccion2.js
          - SeccionCaso.js
          - predicciones_2025.js
        - App.js
        - index.js
        - logo.svg
        - styles.css
      - .gitignore
      - README.md
      - package-lock.json
      - package.json
  - server.py

- README.md

5. Configuración

- La carpeta algoritmos_iniciales esta compuesta por los distintos algoritmos de optimización que se han intentado realizar
  pero sin éxito y de un notebook de las gráficas del EDA.
- **Si quieres ejecutar solamente los algoritmos de cada caso de uso que se encuentran en la carpeta algoritmos, simplemente dirijete al archivo y dale a ejecutar.**
- **Si quieres ejecutar la web que muestra todos los resultados (tarda mucho en ejecutar ya que por cada caso de uso hace una comprobación y después lo vuelve a ejecutar) sigue los pasos que se encuentran en el manual de usuario.**
- **Para instalar las dependencias necesarias para ejecutar el paso anterior ir a la carpeta/react/rutas-app e instalar las dependencias del archivo package.json.**
