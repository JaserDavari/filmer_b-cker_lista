import streamlit as st
import Funktioner

st.set_page_config(layout="wide",
                   page_title="Jasers bok- och filmlista",
                   page_icon=":books:")

st.title("Jasers bok- och filmlista")
st.write("Här kan du lägga till <b>filmer och böcker som du rekommenderar Jazz.</b>",
         unsafe_allow_html=True)

def add_todo():
    item = st.session_state["new_todo"]
    if item:
        Funktioner.write_listan(item)
        st.session_state["new_todo"] = ""

col1, col2 = st.columns([1, 2])
with col1:
    st.text_input("Skriv en ny bok/film:", placeholder="Skriv här...",
                  on_change=add_todo, key="new_todo")

listan = Funktioner.hämta_listan()

for item in listan:
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        Funktioner.ta_bort(item)
        st.rerun()