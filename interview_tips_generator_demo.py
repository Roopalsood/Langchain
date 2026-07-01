from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import PromptTemplate

try:

    llm = ChatOllama(model="gemma:2b")
    prompt_template = PromptTemplate(
        input_variables=["company_name", "position_title", "strength", "weakness"],
        template="""You are an expert in giving out tips for interview. You provide information about a specific job role and its expectations from a specific company, position title and my strengths and weaknesses.
        Avoid giving information about fictional companies. If company is fictional or non-existent answer: I don't know. 
        Answer the question: What are the interview tips for {position_title} in {company_name} if my strength is {strength} and weakness {weakness}? 
        """
    )

    st.title("Interview Tips Generator")
    
    company_name = st.text_input("Enter the company name:")
    position_title = st.text_input("Enter the position title:")
    strength = st.text_input("Enter your strength:")
    weakness = st.text_input("Enter your weakness:")
    
    if company_name and position_title and strength and weakness:            
        response = llm.invoke(prompt_template.format(company_name=company_name, position_title=position_title, strength=strength, weakness=weakness))
        st.write(response.content)    

except Exception as e:
    print("Error: ", e)
    
    
#run in terminal as "streamlit run filename"