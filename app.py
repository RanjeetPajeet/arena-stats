from data import *
from misc import *
import streamlit as st


st.set_page_config(
    page_title="Arena Stats",
    layout="centered",
    page_icon=":crossed_swords:"
)
hide_element("footer", "class", "css-1lsmgbg egzxvld0")


def spacer():
  st.markdown("## ")
 


if 'arena_data' not in st.session_state:
    st.session_state.arena_data = None

    

# ---------------------------------------------------------------------- #



st.markdown("# Arena Stats")
spacer()



tab1, tab2, tab3 = st.tabs(["**2v2**", "**3v3**", "**5v5**"])

with tab1:
   st.header("2v2 Data")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("3v3 Data")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("5v5 Data")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
