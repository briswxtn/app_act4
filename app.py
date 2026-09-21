import streamlit as st
st.title("Clasificador de temperatura")
temperatura = st.number_input(
  "Introducir temperatura en °C: ",
  value=20
)
if temperatura < 20:
  st.write("Hace frío")
elif temperatura < 30:
  st.write("La temperatura es agradable")
else:
  st.write("Hace calor")

