from data import *
import streamlit as st


st.set_page_config(
    page_title="Arena Stats",
    layout="centered",
    page_icon=":crossed_swords:"
)


def spacer():
  st.markdown("##")
 


if 'arena_data' not in st.session_state:
    st.session_state.arena_data = None

    

# ---------------------------------------------------------------------- #



st.markdown("# Arena Stats")
st.markdown("---")



tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
