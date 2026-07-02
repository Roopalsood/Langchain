from langchain_ollama import ChatOllama
import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

try:
    llm1 = ChatOllama(model="gemma:2b")
    llm2 = ChatOllama(model="llama3.2:1b")

    title_prompt = PromptTemplate(
        input_variables=["topic"],
        template = """You are an experienced speech writer. You need to craft an impactful title for a speech on topic: {topic}
        Answer exactly with one title.
        """ 
    )
    
    speech_prompt = PromptTemplate(
        input_variables=["title"],
        template = """You need to write a powerful speech of 350 words for the following title:
        {title}
        """ 
    )
    
    
    first_chain = title_prompt | llm1 | StrOutputParser() | (lambda title: (st.write(title), title)[1]) #1 is title since (st.write(title), title) returns a tuple and we want the second element.
    
    second_chain = speech_prompt | llm2
    
    final_chain = first_chain | second_chain
    
    st.title("Speech Generator")
    
    topic = st.text_input("Enter the topic:")

    if topic:
        response = final_chain.invoke({"topic": topic})
        st.write(response.content)
        
except Exception as e:
    print("Error: ", e)