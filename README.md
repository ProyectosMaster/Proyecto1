# P1_Mercancias_perecederas
1. Objetivos principales
  -	Minimizar coste total: Optimizar las rutas de entrega para reducir el coste total, teniendo en cuenta tanto el coste por kilómetro de cada vehículo como el uso eficiente de la capacidad de carga y la autonomía.
  -	Maximizar el número de pedidos entregados: Planificar las rutas para entregar el mayor número de pedidos posible dentro de las limitaciones de los recursos disponibles (vehículos, capacidad de carga, autonomía, etc.), maximizando la eficiencia operativa.
2. Restricciones
  - Capacidad de carga de los vehículos: Cada vehículo tiene una capacidad máxima de carga en kilogramos que no debe excederse, por lo que los pedidos deben ser distribuidos eficientemente 
  entre los vehículos disponibles. 
  - Autonomía limitada de los vehículos: Cada vehículo tiene una autonomía máxima en kilómetros. Las rutas deben ser ajustadas para que ningún vehículo supere su autonomía durante el día de 
  operación.
  - Considera que el vehículo puede necesitar retornar a su punto de inicio, por lo que la autonomía se debe planificar de forma adecuada.
  - Todas las rutas empiezan y acaban en el almacén

3.	Datos 
  - Tabla flota vehículos  df_vehicle
  -	Tabla localizaciones (almacén y clientes)  df_location
  -	Matriz distancias entre localizaciones en km  df_distance_km
  -	Matriz distancias entre localizaciones en tiempo  df_distance_min
  -	Tabla de pedidos  df_orders
  -	Histórico de pedidos   df_historic_order_demand

4. Estructura de carpetas
  - Profiling:
      -Readme.md
      -df_distance_km.html
      -df_distance_min.html
      -df_historic_order_demand.html
      -df_location.html
      -df_orders.html
      -df_vehicle.html
    
  - Datos/raw_data:
      -prediccion:
           - Readme.md
           - pedidos_2025.csv
      -df_distance_km.xlsx
      -df_distance_min.xlsx
      -df_historic_order_demand.xlsx
      -df_location.xlsx
      -df_orders.xlsx
      -df_vehicle.xlsx
    
  - Documentacion:
      - Business_understanding.docx

  -Modelos:
      - algorimto_djikstra.ipynb
      - algoritmoGenetico.py
      - algoritmoGenetico_caso1_bucle.py
      - algoritmoGenetico_caso2_bucle.py 
      - algoritmoGenetico_caso3.py
      - algoritmo_ortools.py
      - algoritmo_programacion_lineal.py

  -Script: 
      - predicciones_enero2025_bueno.ipynb

  -README.md




    

    

