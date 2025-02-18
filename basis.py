import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título y descripción
st.title("Dashboard Educativo Interactivo")
st.subheader("Una herramienta de aprendizaje divertida")

# Función para cambiar el modo
modo = st.sidebar.selectbox("Selecciona el modo", ["claro", "oscuro"])
st.markdown(f'<style>body{{background-color: {"#ffffff" if modo == "claro" else "#333333"}; color: {"#000000" if modo == "claro" else "#ffffff"};}}</style>', unsafe_allow_html=True)

# Progreso del día
progreso = 784
st.header("Progreso del Día")
fig, ax = plt.subplots()
circle = plt.Circle((0.5, 0.5), 0.4, color="#eee", lw=3, fill=False)
ax.add_artist(circle)
circle = plt.Circle((0.5, 0.5), 0.4, color="#4CAF50", lw=3, fill=False, transform=ax.transAxes, clip_on=False, theta1=0, theta2=(progreso/1000)*360)
ax.add_artist(circle)
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)

# Actividades del Mes
datos_grafica = pd.DataFrame({
    'mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'valor': [30, 45, 35, 50, 40]
})

st.header("Actividades del Mes")
st.line_chart(datos_grafica)

# Amiguitos de Hoy
estudiantes = [
    {"nombre": "Sarah Hudson", "hora": "10:00"},
    {"nombre": "Dakota Smith", "hora": "11:15"},
    {"nombre": "John Lane", "hora": "12:30"}
]

st.header("Amiguitos de Hoy")
for estudiante in estudiantes:
    st.text(f"{estudiante['nombre']} - {estudiante['hora']}")

# Eventos Divertidos
eventos = [
    {"tipo": "Reunión de equipo", "participantes": 3},
    {"tipo": "Clase de arte", "participantes": 2}
]

st.header("Eventos Divertidos")
for evento in eventos:
    st.text(f"{evento['tipo']} - {evento['participantes']} participantes")
