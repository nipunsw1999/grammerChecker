import streamlit  as st

def logo():
    col1,col2 = st.columns([3,2])
    with col1:
        st.title("Grammer Checker")
    with col2:
        st.image('logo.png',width=100)