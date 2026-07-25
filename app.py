import streamlit as st
import numpy as np

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
  st.write("Estas en el módulo de arreglos")
  valor_inicial = st.number_input("Ingrese el valor inicial", value = 0)
  valor_final = st.number_input("Ingrese el valor final", value = 1)
  lista_numerica = list(range(valor_inicial, valor_final))
  st.write(lista_numerica)
  limite_inferior = st.number_input("Ingrese el límite inferior:", value = 1200)
  limite_superior = st.number_input("Ingrese el límite superior:", value = 1250)
  cantidad_datos = st.number_input("Ingres la totalidad de datos a crear:", value = 31)
  datos_produccion = np.random.randint(limite_inferior, limite_superior, cantidad_datos)
  st.write(datos_produccion)
  st.write("La producción total es: ", np.sum(datos_produccion))
  st.write("La producción promedio es: ", np.mean(datos_produccion))

elif modulo == "Ejercicio 2":
  st.subheader("Ejercicio 2")

elif modulo == "Ejercicio 3":
  st.title("Ejercicio 3")
else:
  st.write("Ejercicio 4")
