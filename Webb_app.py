import streamlit as st
import Funktioner

listan = Funktioner.hämta_listan()

def add_todo():
    lista = st.session_state["new_todo"]
    listan.append(lista + "\n")
    Funktioner.write_listan(listan)
    st.session_state["new_todo"] = ""


listan = Funktioner.hämta_listan()

st.set_page_config(layout="wide", 
                   page_title="Jasers bok- och filmlista", 
                   page_icon=":books:")

st.title("Jasers bok- och filmlista")
st.write("Här kan du lägga till <b>filmer och böcker som du vill se.</b>", 
         unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])
with col1:
    st.text_input("Skriv en ny bok/film:", placeholder="Skriv här...",
                  on_change=add_todo, key="new_todo")


for index, lista in enumerate(listan):
    checkbox = st.checkbox(lista, key=lista)
    if checkbox:
        listan.pop(index)
        Funktioner.write_listan(listan)
        del st.session_state[lista]
        st.rerun()
        st.success(f"Uppgiften '{lista.strip()}' är nu markerad som klar.") 
