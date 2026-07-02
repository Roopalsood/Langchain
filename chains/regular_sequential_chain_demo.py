from langchain_ollama import ChatOllama
import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

try:
    llm1 = ChatOllama(model="gemma:2b")

    title_prompt = PromptTemplate(
        input_variables=["topic"],
        template = """You are an experienced speech writer. You need to craft an impactful title for a speech on topic: {topic}
        Answer exactly with one title.
        """ 
    )
    
    speech_prompt = PromptTemplate(
        input_variables=["title","Emotion"],
        template = """You need to write a powerful speech of 350 words for the following title:
        {title} with {emotion}.
        Format the output with 2 keys: 'title' and 'speech'. The value of 'title' should be the title of the speech and the value of 'speech' should be the speech itself.
        """ 
    )
    
    
    first_chain = title_prompt | llm1 | StrOutputParser() | (lambda title: (st.write(title), title)[1]) #1 is title since (st.write(title), title) returns a tuple and we want the second element.
    
    second_chain = speech_prompt | llm1 | JsonOutputParser()
    
    final_chain = first_chain | (lambda title: {"title":title, "emotion":emotion} ) | second_chain
    
    st.title("Speech Generator")
    
    topic = st.text_input("Enter the topic:")
    emotion = st.text_input("Enter the emotion:")

    if topic and emotion:
        response = final_chain.invoke({"topic": topic})
        st.write(response)
        st.write("Title: ", response["title"])
        
except Exception as e:
    print("Error: ", e)