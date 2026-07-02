"""
This script demonstrates how to use the Langchain library with OpenAI's GPT-3.5-turbo model.
It initializes a ChatOpenAI instance with the provided API key, prompts the user for a question,
and retrieves a response from the model. If there is an error related to OpenAI's API, it catches
the exception and prints an error message indicating that the credits are exhausted.

Dependencies:
- langchain_openai: For interacting with OpenAI's models.
- openai: For handling OpenAI-specific errors.

Usage:
1. Ensure that the OPENAI_API_KEY is set in the config module.
2. Run the script and enter a question when prompted.
3. The response from the model will be printed to the console.
"""

from config import OPENAI_API_KEY

from langchain_openai import ChatOpenAI
from openai import OpenAIError

try: 
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
    question = input("Enter the question: ")

    response = llm.invoke(question)
    print(response)
    
except OpenAIError as e:
    print("Credits exhausted ", e)