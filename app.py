from data import *
from misc import *
from plots import *
import numpy as np
# import streamlit as st


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
    
if 's6_data_2v2' not in st.session_state:
    st.session_state.s6_data_2v2 = get_s6_2v2_data()

if 's6_data_3v3' not in st.session_state:
    st.session_state.s6_data_3v3 = get_s6_3v3_data()

if 's6_data_5v5' not in st.session_state:
    st.session_state.s6_data_5v5 = get_s6_5v5_data()



# ---------------------------------------------------------------------- #



st.markdown("# Arena Stats")
st.markdown("---")


season_6 = st.checkbox("Season 6", value=True)
spacer()




tab1, tab2, tab3, point_calculator_tab = st.tabs(["**2v2**", "**3v3**", "**5v5**", "**AP Calculator**"])


with tab1:
    spacer()
    
    if season_6:
        st.header("Season 6 2v2 Data")
        if st.session_state.s6_data_2v2 is not None:
            st.write(st.session_state.s6_data_2v2[::-1])
            spacer()
            per_comp_2v2, per_map_2v2 = st.columns(2)
            with per_comp_2v2:
                st.markdown("### Winrates per comp")
                st.write(get_2v2_winrates(st.session_state.s6_data_2v2))
            with per_map_2v2:
                st.markdown("### Winrates per map")
                st.write(get_2v2_winrates_per_map(st.session_state.s6_data_2v2))
            spacer()
            st.markdown("### Rating over time")
            st.write(plot_data(st.session_state.s6_data_2v2))
    
    else:
        st.header("Season 5 2v2 Data")
        if st.session_state.data_2v2 is not None:
            s5_data_2v2 = get_s5_2v2_data()
            st.write(s5_data_2v2[::-1])
            spacer()
            per_comp_2v2, per_map_2v2 = st.columns(2)
            with per_comp_2v2:
                st.markdown("### Winrates per comp")
                st.write(get_2v2_winrates(s5_data_2v2))
            with per_map_2v2:
                st.markdown("### Winrates per map")
                st.write(get_2v2_winrates_per_map(s5_data_2v2))
            spacer()
            st.markdown("### Rating over time")
            st.write(plot_data(s5_data_2v2))



with tab2:
    spacer()
    
    if season_6:
        st.header("Season 6 3v3 Data")
        if st.session_state.s6_data_3v3 is not None:
            st.write(st.session_state.s6_data_3v3[::-1])
            spacer()
            st.markdown("### Winrates per map")
            st.write(get_3v3_winrates_per_map(st.session_state.s6_data_3v3))
            st.markdown("### Winrates per comp")
            st.write(get_3v3_winrates(st.session_state.s6_data_3v3))
            spacer()
            st.markdown("### Rating over time")
            st.write(plot_data(st.session_state.s6_data_3v3,True))
    
    else:
        st.header("Season 5 3v3 Data")
        if st.session_state.data_3v3 is not None:
            s5_data_3v3 = get_s5_3v3_data()
            st.write(s5_data_3v3[::-1])
            spacer()
            st.markdown("### Winrates per map")
            st.write(get_3v3_winrates_per_map(s5_data_3v3))
            st.markdown("### Winrates per comp")
            st.write(get_3v3_winrates(s5_data_3v3))
            spacer()
            st.markdown("### Rating over time")
            st.write(plot_data(s5_data_3v3,True))



with tab3:
    spacer()
    
    if season_6:
        st.header("Season 6 5v5 Data")
    
    else:
        st.header("Season 5 5v5 Data")
        if st.session_state.data_5v5 is not None:
            st.write(st.session_state.data_5v5[::-1])
            spacer()
            st.markdown("### Rating over time")

            
            
            
            
with point_calculator_tab:
    spacer()
    
    with st.form(key="ap_calculator"):
        st.write("Arena Point estimation")
        col2, col3, col5 = st.columns(3)
        with col2:
            check2v2 = st.checkbox("2v2")
        with col3:
            check3v3 = st.checkbox("3v3")
        with col5:
            check5v5 = st.checkbox("5v5")
        col_rating, col_submit = st.columns(2)
        with col_rating:
            arena_rating = st.number_input("Rating", min_value=0, max_value=3000, value=0, step=1)
        with col_submit:
            submitted = st.form_submit_button("Submit")
        if submitted:
            if arena_rating > 1500:
                points = 1511.26 / ( 1 + (1639.28*np.exp(-0.00412*arena_rating)) )
            else:
                points = 0.22*arena_rating + 14
            if check2v2:
                points = points*0.76
            elif check3v3:
                points = points*0.88
            points = int(points)
            
            spacer()
            st.write(f"Estimated points: {points}")
