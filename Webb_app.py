import streamlit as st
import Funktioner

listan = Funktioner.hämta_listan()

def add_todo():
    lista = st.session_state["new_todo"]
    listan.append(lista + "\n")
    Funktioner.write_listan(listan)
    st.session_state["new_todo"] = ""


listan = Funktioner.hämta_listan()

st.title("Min to-do lista")
st.write("Här kan du lägga till, ta bort och markera uppgifter som slutförda.")

for index, lista in enumerate(listan):
    checkbox = st.checkbox(lista, key=lista)
    if checkbox:
        listan.pop(index)
        Funktioner.write_listan(listan)
        del st.session_state[lista]
        st.rerun()
        st.success(f"Uppgiften '{lista.strip()}' är nu markerad som klar.") 

st.text_input("Skriv en uppgift:", placeholder="Skriv här...",
              on_change=add_todo, key="new_todo")
