import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from key import OPEN_API_KEY
import streamlit as st
import time

os.environ["OPENAI_API_KEY"] = OPEN_API_KEY

llm = OpenAI(temperature=0.7)

def grammer_checker(act,txt):
    prompt_template_name = PromptTemplate(
        input_variables= ['act','txt'],
        template= "You act as : {act}, Check this grammer and correct it : {txt}"
    )
    start = time.time()
    with st.status("Grammer checking...", expanded=True) as status:
        chain = LLMChain(llm=llm, prompt=prompt_template_name)
        response = chain.run({"act":act,"txt":txt})
        end = time.time()
        est = end-start
        status.update(label=f"Checked! in {est:.2f} seconds",state = "complete",expanded=False)
    return response