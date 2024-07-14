import streamlit as st
import streamlit_option_menu
import functions
from langchain_help import grammer_checker

st.title("Grammer Checker")

text = st.text_area("Enter your text")
act = st.selectbox("Act as",("Teacher","Creative Writer","Poet"))
check = st.button("Check grammer")

if check:
    if not text:
        functions.warn("Enter any text",2)
    elif not len(text)>3:
        functions.warn("Enter a valid text",2)
    else:
        st.write(grammer_checker(act,text))
        functions.completed("Done",2)
    