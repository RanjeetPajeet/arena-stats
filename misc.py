import streamlit as st




def run_custom_css(css: str):
    """
    Runs the given string as a CSS expression.
    """
    import streamlit as st
    st.markdown("<style>" + css + "</style>", unsafe_allow_html=True)

    
    
def run_custom_javascript(code: str):
    """
    Runs the given Javascript code.
    """
    from streamlit.components.v1 import html
    html(f"<script>{code}</script>")

    
    
def hide_element(element: str, attribute_name: str, attribute_value: str):
    """
    Hides an element with the given identifiers.
    """
    run_custom_css(f'{element}[{attribute_name}="{attribute_value}"]' + '{display: none;}')
