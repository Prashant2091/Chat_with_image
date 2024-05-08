import os
# from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")

def response(prompt, query, image):
    response = model.generate_content([query,image,prompt])
    return response.text

def image_data(file):
    if file is not None:
        data = file.getvalue()

        image = [{"mime_type":file.type,
                  "data":data}]
        
        return image
    else:
        st.error("Upload file")

st.header("Chat with Picture")

file = st.file_uploader("Upload Picture",type=["png","jpg","jpeg"])

input_prompt="""
You are an expert in understanding Pictures. We will upload a a image 
and you will have to answer any questions based on the uploaded image
"""

if file is not None:
    image = Image.open(file)
    st.image(image=image)

if file is not None:
    input=st.text_input("Input Prompt: ",key="input")

button = st.button('submit')
if button:
    image = image_data(file)
    response = response(input_prompt,query=input, image=image[0])
    st.subheader("Response:")
    st.write(response)
