import streamlit as st
import numpy as np
import pandas as pd

st.sidebar.title("Indice")

modulo = st.sidebar.selectbox("Elija una sección", ["Home", "Ejercicio 1","Ejercicio 2","Ejercicio 3","Ejercicio 4"])

if modulo == "Home":
  st.title("Proyecto Módulo 1 Fundamentals")
  st.image("Python_logo.png")
  st.subheader("Nombre del alumno:")
  st.write("Hernan Martin Cristobal Ramos")
  st.subheader("Nombre del módulo:")
  st.write("Módulo Python Fundamentals")
  st.subheader("Información del estudiante:")
  st.write("Ingeniero Industrial con más de 9 años de experiencia en el rubro de banca y seguros en analítica de datos y gestión de productos")
  st.subheader("Descripción del proyecto:")
  st.write("Desarrollar una aplicación interactiva en Streamlit que integre los conceptos del Módulo 1 del curso: variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos.")
  st.subheader("Tecnologías usadas:")
  st.write("Python, Github, Sreamlit")
  st.markdown("***2026***")
  
elif modulo == "Ejercicio 1":
  # Titulo y descripción del ejercicio
  st.title("Ejercicio 1")
  st.markdown("""### Descripción
  Registre los movimientos financieros. Cada movimiento debe tener:
  - Concepto
  - Tipo de movimiento (Ingreso o Gasto)
  - Valor
  
  La aplicación mostrará el total de ingresos, gastos, saldo y el estado del flujo de caja (a favor o en contra).""")
  # Crear la lista
  if "movimientos" not in st.session_state:
    st.session_state.movimientos = []
  #Registrar entradas
  concepto = st.text_input("Concepto: ")
  tipo = st.selectbox("Movimiento: ", ["Ingreso","Gasto"])
  valor = st.number_input("Valor: ", value = 0)
  # Botón para agregar a la lista
  if st.button ("Agregar movimiento"):
    if concepto != "" and valor > 0:
      movimiento = {"Concepto": concepto, "Tipo": tipo, "Valor": valor}
      st.session_state.movimientos.append(movimiento)
      st.success("Movimiento agregado")
    else:
      st.error("Debe ingresar un concepto y un valor")
  # Mostrar tabla
  if st.session_state.movimientos:
    df = pd.DataFrame(st.session_state.movimientos)
    st.subheader("Movimientos registrados")
    st.dataframe(df, use_container_width = True)
  # Calculos
    ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
    gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()
    saldo = ingresos - gastos
  # Resultados
    st.subheader("Resultados")
    st.metric("Total ingresos", ingresos)
    st.metric("Total gastos", gastos)
    st.metric("Saldo", saldo)
    if saldo >= 0:
      st.success("Flujo de caja a favor.")
    else:
      st.error("Flujo de caja en contra.")
  else:
    st.info("No hay movimientos registrados")


elif modulo == "Ejercicio 2":
  # Titulo y descripción del ejercicio
  st.title("Ejercicio 2")
  st.markdown("""### Descripción
  Crear un formulario para registrar productos usando NumPy. Cada registro contiente:
  - Nombre del producto
  - Categoría
  - Precio
  - Cantidad
  - Total
  
  Los datos serán almacendos en arrays y convertidos en un DataFrame. """)
  # Crear array
  if "productos" not in st.session_state:
    st.session_state.productos = np.empty((0,5), dtype = object)
  # Formulario para registrar los productos
  producto = st.text_input("Nombre:")
  categoria = st.selectbox("Categoría:",["Alimentos","Bebidas","Tecnología","Deportes","Ropa","Juguetes","Otros"])
  precio = st.number_input("Precio:", value = 0.50, min_value = 0.50)
  cantidad = st.number_input("Cantidad:", value = 1, min_value = 1)
  total = round(precio * cantidad, 2)
  # Botón para agregar
  if st.button("Agregar producto"):
    if producto != "" and precio >= 0.50 and cantidad >= 1:
      registro = np.array([[producto, categoria, precio, cantidad, total]])
      st.session_state.productos = np.vstack([st.session_state.productos, registro])
      st.success("Producto agregado correctamente")
    else:
      st.error("Ingrese un nombre, un precio valido y una cantidad")
  # Mostrar DataFrame
  if len(st.session_state.productos) > 0:
    columnas = ["Producto","Categoría","Precio","Cantidad","Total"]
    df = pd.DataFrame(st.session_state.productos,columns=columnas)
    st.subheader("Lista de Productos")
    st.dataframe(df,use_container_width=True)
  else:
    st.info("No hay productos registrados")


elif modulo == "Ejercicio 3":
  #Importamos la funcion
  from libreria_funciones_proyecto1 import calcular_roi
  # Titulo y descripción del ejercicio
  st.title("Ejercicio 3")
  st.markdown("""### Descripción
  Esta aplicación utiliza un función externa para calcular el ROI, se debe ingresar:
  - Ganancia neta
  - Inversion
  
  Se calculará el ROI y un historial de resultados. """)
  # Crear lista
  if "historial" not in st.session_state:
    st.session_state.historial = []
  # Selector de función
  funcion = st.selectbox("Seleccione función:",["Calcular ROI"])
  # Widgets según función
  if funcion == "Calcular ROI":
    ganancia = st.number_input("Ganancia neta:",value = 0)
    inversion = st.number_input("Inversión:",value = 0, min_value = 0)
  #Ejecutar función
  if st.button ("Ejecutar función"):
    if inversion > 0:
      resultado = calcular_roi(ganancia, inversion)
      st.subheader("Restulado")
      st.success(f"ROI obtenido: {resultado['roi_pct']} %")
      # Guardar histórico
      registro = {"Función": funcion,"Ganancia neta": ganancia,"Inversión": inversion,"ROI (%)": resultado["roi_pct"]}
      st.session_state.historial.append(registro)
    else:
      st.error("La inversión debe ser mayor a cero")
  # Mostrar histórico
  if st.session_state.historial:
    st.subheader("Histórico de resultados")
    df = pd.DataFrame(st.session_state.historial)
    st.dataframe(df, use_container_width=True)


else:
  # Importamos la función
  from libreria_clases_proyecto1 import ProyectoInversion
  # Título y descripción del ejercicio
  st.title("Ejercicio 4")
  st.markdown("""### Descripción
  Esta aplicación utiliza una clase externa llamada ProyectoInversion.
  Permite registrar proyectos de inversión y realizar operaciones CRUD:
  - Crear proyectos
  - Leer proyectos registrados
  - Actualizar información
  - Eliminar proyectos
  
  Además calcula:
  - VPN
  - ROI
  - Payback
  - Decisión de viabilidad""")
  # Almacenar objetos
  if "proyectos" not in st.session_state:
    st.session_state.proyectos = []
  # Crear pestañas
  tab1, tab2, tab3 = st.tabs(["Crear proyecto", "Actualizar / Eliminar", "Resultados"])
  # Crear
  with tab1:
    st.subheader("Nuevo proyecto")
    nombre = st.text_input("Ingrese nombre del proyecto:")
    inversion = st.number_input("Inversion inicial:",value = 0, min_value = 0)
    flujos_texto = st.text_input("Flujos de caja separados por coma", placeholder = "Ejemplo: 5000, 6000, 7000")
    tasa = st.number_input("Tasa de descuento (%)", min_value = 0.0)
    if st.button("Crear proyecto"):
      try:
        flujos = [float(x) for x in flujos_texto.split(",")]
        proyecto = ProyectoInversion(nombre, inversion, flujos,tasa)
        st.session_state.proyectos.append(proyecto)
        st.success("Proyecto creado correctamente")
      except Exception as e:
        st.error(e)
   # Actualizar / Eliminar
  with tab2:
    st.subheader("Gestión de proyectos")
    if st.session_state.proyectos:
      nombres = [p.nombre_proyecto for p in st.session_state.proyectos]
      seleccionado = st.selectbox("Seleccione proyecto:", nombres)
      indice = nombres.index(seleccionado)
      proyecto = st.session_state.proyectos[indice]
      nuevo_nombre = st.text_input("Nuevo nombre", value = proyecto.nombre_proyecto)
      if st.button ("Actualizar"):
        proyecto.nombre_proyecto = nuevo_nombre
        st.success("Proyecto actualizado")
      if st.button ("Eliminar"):
        st.session_state.proyectos.pop(indice)
        st.success("Proyecto eliminado")
    else:
      st.info("No existen proyectos registrados")
  # Leer resultados
  with tab3:
    st.subheader("Proyectos registrados")
    if st.session_state.proyectos:
      datos =[]
      for proyecto in st.session_state.proyectos:
        datos.append(proyecto.resumen())
      df = pd.DataFrame(datos)
      st.dataframe(df, use_container_width = True)
      st.subheader("Indicadores")
      proyecto_sel = st.selectbox("Ver detalle",df["proyecto"])
      resultado = df[df["proyecto"] == proyecto_sel].iloc[0]
      st.metric("VPN",f"{resultado['vpn']:.2f}")
      st.metric("ROI",f"{resultado['roi_pct']} %")
      st.metric("Payback",f"{resultado['payback_anios']} años")
      if resultado["decision"] == "Viable":
        st.success("Proyecto viable")
      else:
        st.error("Proyecto no viable")
    else:
      st.info("No hay proyectos registrados")
