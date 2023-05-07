# import cv2
import streamlit as st
from datetime import datetime
from deepface import DeepFace
from PIL import Image


user_name = st.text_input("Enter your name")

# Get user's email
email = st.text_input("Enter your email")


capture_confirmation = st.checkbox("Capture Photo")

if capture_confirmation:
    picture = st.camera_input("First, take a picture...")

    if picture:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{user_name}{timestamp}.jpg"

        with open(file_name, 'wb') as file:
            file.write(picture.getbuffer())

        st.success(f"Photo captured and saved as {file_name}!")

        # Load the captured photo using PIL
        image = Image.open(file_name)

        # Perform emotion analysis using DeepFace
        result = DeepFace.analyze(img_path=file_name, actions=['age', 'gender', 'race'], enforce_detection=False, )

        # Get the dominant emotion
        guess = result

        # Display the dominant emotion
        st.write("Age must be:", guess)