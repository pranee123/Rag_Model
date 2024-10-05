## Application that can take the Image as an Input 
## We write a prompt and then LLM should connect the prompt with Image
## and Generate the Output

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() # Enable the Local Environment Variables..
from PIL import Image # This will store the Image
import io

# Configure genai
genai.configure(api_key=os.getenv("Google-Api-Key"))
# Prepare the Frontend
st.header("🎯Image to Text Generator📝",divider = "green")
user_input = st.text_input("✏️Input Prompt: ")
file_upload = st.file_uploader("Upload the Image...",type = ["JPG","JPEG","PNG"])
# Display the Image
img = ""
# if file_upload: 
if file_upload is not None:
    img = Image.open(file_upload)
    st.image(img,caption="Image Uplodaded",use_column_width=True)
# Function for response
def gemini_response(user_input,img):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    if user_input != "":
        response = model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text
# Create the Button
submit = st.button("Click here")
if submit:
    response = gemini_response(user_input=user_input,img=img)
    st.subheader("The Response is:",divider = True)
    st.write(response)
