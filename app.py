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

if 'data_2v2' not in st.session_state:
    st.session_state.data_2v2 = get_2v2_data()

if 'data_3v3' not in st.session_state:
    st.session_state.data_3v3 = get_3v3_data()

if 'data_5v5' not in st.session_state:
    st.session_state.data_5v5 = get_5v5_data()

    

# ---------------------------------------------------------------------- #



st.markdown("# Arena Stats")
spacer()



tab1, tab2, tab3 = st.tabs(["**2v2**", "**3v3**", "**5v5**"])

with tab1:
    st.header("2v2 Data")
    if st.session_state.data_2v2 is not None:
        st.write(st.session_state.data_2v2[::-1])
        spacer()
        st.markdown("### Winrates")
        st.write(get_2v2_winrates(st.session_state.data_2v2))
        spacer()
        st.markdown("## Rating over time")
        

with tab2:
    st.header("3v3 Data")
    if st.session_state.data_3v3 is not None:
        st.write(st.session_state.data_3v3[::-1])
        spacer()
        st.markdown("### Winrates")
        st.write(get_3v3_winrates(st.session_state.data_3v3))
        spacer()
        st.markdown("### Rating over time")

with tab3:
    st.header("5v5 Data")
    if st.session_state.data_5v5 is not None:
        st.write(st.session_state.data_5v5[::-1])
        spacer()
        st.markdown("### Rating over time")
