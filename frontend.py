import pandas as pd
import streamlit as st
from llama_index.core import Document, VectorStoreIndex
import openai
import os
import requests
import pandas as pd
import time
# from dotenv import load_dotenv
# load_dotenv()

# # Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Example DataFrame with restaurant data

df = pd.read_csv("/Users/kirindesai/Desktop/Foodie-Finder/berkeley50.csv")
print(type(df['text']))
df.head(10)


st.set_page_config(page_title="Foodie Finder", layout="wide")
st.title("🍽️ Foodie Finder")
st.subheader(f"Discover the Best Restaurants in Berkeley")
st.markdown(f"""
### Welcome to Foodie Finder!
Find the best places to eat in Berkeley. 
We provide comprehensive reviews, ratings, and essential details to enhance your dining experience.
""")
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f5;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Create text representation for each restaurant
df['text'] = (
    "Name: " + df['Name'] + 
    " - Location: " + df['Location'] + 
    " - Rating: " + df['Rating'].astype(str) + 
    " - # of reviews: " + df['Review Count'].astype(str) + 
    " - Price: " + df['Price'] + 
    " - Categories: " + df['Categories'] + 
    " - Reviews: " + df['Reviews']
)

# Create documents from the DataFrame
documents = [Document(text=row['text']) for _, row in df.iterrows()]

# Build the index
index = VectorStoreIndex.from_documents(documents)

# Streamlit app layout
st.title("Foodie Finder")
st.subheader(f"Find the best restaurants in Berkeley!")

# Input for the user query
user_query = st.text_input("Ask a question about restaurants:")

if st.button("Get Answer"):
    if user_query:
        # Query the index and generate a response
        eng = index.as_chat_engine()
        response = eng.query(user_query)

        # Output the response
        st.write(f"**Response:** {response}")
    else:
        st.error("Please enter a question.")
