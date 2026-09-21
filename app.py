import streamlit as st
st.title("Clasificador de temperatura")
temperatura = st.number_input(
  "Introducir temperatura en °C:".
  value=20
)

if temperatura＜20:
  st.writte("Hace frío")
elif temperatura＜30:
  st.writte("La temperatura es agradable")
else:
  st.writte("Hace calor")
