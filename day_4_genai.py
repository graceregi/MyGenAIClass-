from  google import genai;
import streamlit as st;

st.title("My first streamlit app")
robo = genai.Client(api_key=st.secrets["your_api_key"])
question = st.text_input("Enter your prompt : ")
mychat = robo.chats.create(model="gemini-3.1-flash-lite")

if st.button("Send"):
    response = mychat.send_message(question)
    st.write(response.text)
