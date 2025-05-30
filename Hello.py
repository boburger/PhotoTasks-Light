import streamlit as st
   
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Fotografische Aufgaben")
st.sidebar.success("Wählen Sie oben eine Aufgabe aus.")

st.markdown(
    """
    Mit diesen fotografischen Aufgaben sollen die Lernenden systematisch verschiedene fotografische Techniken,
    Themenbereiche und kreative Herangehensweisen kennenlernen.
    **👈 Wählen Sie eine Aufgabe in der Menüleiste**
    ### Aufgaben:
    - Aufgabe #1 - Bad Photos
    - Aufgabe #2 - Sports and Action
    - Aufgabe #3 - Macro Photography
    - Aufgabe #4 - Architecture and Interiors
    - Aufgabe #5 - Still Life
    - Aufgabe #6 - Landscape and Nature
    - Aufgabe #7 - Night and Color
    - Aufgabe #8 - Portraiture and Light
"""
)