from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate

try:

    llm = ChatOllama(model="gemma:2b")
    prompt_template = PromptTemplate(
        input_variables=["country", "no_of_paras", "language"],
        template="""You are an expert in traditional cuisines. You provide information about a specific dish from a specific country.
        Avoid giving information about fictional places. If country is fictional or non-existent answer: I don't know. 
        Answer the question: What is a traditional cuisine of {country}?
        Answer in {no_of_paras} short paragraphs in {language}."""
    )

    st.title("Cuisine Info")
    
    country = st.text_input("Enter the country:")
    no_of_paras = st.number_input("Enter the number of paragraphs:", min_value=1, max_value=10)
    langugage = st.text_input("Enter the language:")
    
    if country:            
        response = llm.invoke(prompt_template.format(country=country, no_of_paras = no_of_paras, language=langugage))
        st.write(response.content)    

except Exception as e:
    print("Error: ", e)
    
    
#run in terminal as "streamlit run streamlit_demo.py"