from langchain_ollama import ChatOllama
import streamlit as st

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

try:
    llm1 = ChatOllama(model="gemma:2b")

    subject_prompt = PromptTemplate(
        input_variables=["product_name"],
        template = """You are an experienced email writer. You need to craft an impactful subject for marketing on product: {product_name}
        Answer exactly with one liner subject.
        """ 
    )
    
    email_prompt = PromptTemplate(
        input_variables=["subject","no_of_words", "target_audience"],
        template = """You need to write a creative marketing email of {no_of_words} words for the following subject:
        {subject} for the target audience {target_audience}.
        Format the output with 3 keys: 'subject' and 'no_of_words'. The value of 'subject' should be the subject of the email and the value of 'no_of_words' should be the email itself.
        """ 
    )
    
    
    first_chain = subject_prompt | llm1 | StrOutputParser() | (lambda subject: (st.write(subject), subject)[1]) #1 is title since (st.write(title), title) returns a tuple and we want the second element.
    
    second_chain = email_prompt | llm1 | JsonOutputParser()
    
    final_chain = first_chain | (lambda subject: {"subject":subject, "no_of_words": no_of_words, "target_audience": target_audience} ) | second_chain
    
    st.title("Speech Generator")
    
    product_name = st.text_input("Enter the product name:")
    no_of_words = st.number_input("Enter the no of words:", min_value=1, max_value=1000)
    target_audience = st.text_input("Enter the target audience:")

    if product_name and no_of_words and target_audience:
        response = final_chain.invoke({"product_name": product_name})
        st.write(response)
        st.write("Subject: ", response["subject"])
        
except Exception as e:
    print("Error: ", e)