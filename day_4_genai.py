#Streamlit - an ui (to develop the websites, it itself gives html,css noting we need to do,, like a full frontend library )
# to install use the command "pip install streamlit" 
#https://streamlit.io/  refer this link for more information about streamlit 
# (use streamlit cheat sheet for more information about streamlit)
#--------------------------------------------------------------------------------------------------------------------------------

# import streamlit
# streamlit.title("My first streamlit app")

#--------------------------------------------------------------------------------------------------------------------------------
#after giving this command if u run you will get an error because we have not given any command to run the streamlit app
#go to the folder where this file is present open command prompt and run the command "streamlit run day_4_genai.py" in the terminal
#when u do this it will open a new tab in your browser and you will see the title of the app you have given in the code
#and see command prompt it will show the url of the app Local URL: http://localhost:8501 (when u run react u will get local same concept)
#   Network URL: http://192.168.1.7:8501 (this network url is tempporary adress , diffrent networks will have different network url, so if u want to access this app from other device in the same network then use this network url)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# import streamlit as st;
# st.title("My first streamlit app")
# with st.chat_message("user"):
#     st.write("Hello 👋")

#----------------------------------GEN AI WITH STREAMLIT----------------------------------------------------------------------------------------------# 
# from  google import genai;
# import streamlit as st;

# st.title("My first streamlit app")
# robo = genai.Client(api_key="your api key")
# question = st.text_input("Enter your prompt : ")
# response = robo.models.generate_content(
#     model="gemini-3.1-flash-lite",
#     contents=question
# )
# st.write(response.text)
# ------------------------------------------------------------------------------------------------------------------------------------------------
#when u do this u dont have a button to submit the prompt, so we can use a button to submit the prompt and get the response
# from  google import genai;
# import streamlit as st;

# st.title("My first streamlit app")
# robo = genai.Client(api_key="your api key")
# question = st.text_input("Enter your prompt : ")
# mychat = robo.chats.create(model="gemini-3.1-flash-lite")

# if st.button("Send"):
#     response = mychat.send_message(question)
#     st.write(response.text)

#no need of while loop because streamlit will run the code again and again when we click the button, so we can use a button to submit the prompt and get the response
import streamlit as st
from google import genai
st.markdown(
  """
  <h1 style='text-align: center;'> Python AI Assistant</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any Python programming question.
  </p>
  """,
  unsafe_allow_html=True,
)
robo = genai.Client(api_key="your api key")
mychat = robo.chats.create(model="gemini-flash-lite-latest")

# Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")

if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)
# --------------------------------------Deploy into github-----------------------------------------------------------------------------------------
#ope streamlite.io and open github and create a new repository and 
# copy the url of the repository and paste it in the streamlit.io and click on deploy button, it will ask for the github username and password and then it will deploy the app into github
# give file name, commit changes
