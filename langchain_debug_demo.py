from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.globals import set_debug

set_debug(True)

try:

    llm = ChatOllama(model="gemma:2b")

    st.title("Ask gemma")
    
    question = st.text_input("Enter your question:")
    
    if question:            
        response = llm.invoke(question)
        st.write(response.content)    

except Exception as e:
    print("Error: ", e)
    
    
#run in terminal as "streamlit run streamlit_demo.py"