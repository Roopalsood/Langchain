from langchain_ollama import ChatOllama
import streamlit as st

from langchain_core.prompts import PromptTemplate

try:
    llm = ChatOllama(model="gemma:2b")
    prompt_template = PromptTemplate(
        input_variables=["city", "month", "language", "budget"],
        template = """Welcome to the city {city}. You are a travel guide. If you are visiting {city} in the month of {month}, here's what you can do:
        1. Must-visit attractions.
        2. Local cuisine you must try.
        3. Useful phrases in {language}.
        4. Tips for travelling on a {budget} budget.
        
        Enjoy your trip and make the most of your visit to {city} in {month}!
        
        """
        
    )
    
    st.title("Travel Guide")
    
    city = st.text_input("Enter the city:")
    month = st.text_input("Enter the month:")
    language = st.text_input("Enter the language:")
    budget = st.selectbox("Travel Budget", ["Low", "Medium", "High"])
    
    chain = prompt_template | llm
    
    if city and month and language and budget:
        response = chain.invoke({"city":city, "month": month, "language": language, "budget": budget})
        st.write(response.content)
        
except Exception as e:
    print("Error: ", e)