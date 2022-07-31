# We install the FER() library to perform facial recognition
# This installation will also take care of any of the above dependencies if they are missin

from email.mime import image
from fer import FER
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def load_image(image_file):
    img = Image.open(image_file)
    return img


def pred(image_file):
    test_image_one = plt.imread(image_file)
    emo_detector = FER(mtcnn=True)
# Capture all the emotions on the image
    captured_emotions = emo_detector.detect_emotions(test_image_one)
# Print all captured emotions with the image

    plt.imshow(test_image_one)

# Use the top Emotion() function to call for the dominant emotion in the image
    dominant_emotion, emotion_score = emo_detector.top_emotion(test_image_one)
    return dominant_emotion, emotion_score


def main():
    st.title("File Upload of Face")

    menu = ["Image"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image":
        st.subheader("Image")
    image_file = st.file_uploader("Upload_image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        file_details = {"filename": image_file.name,
                        "filetype": image_file.type, "file size": image_file.size}

        st.write(file_details)
        st.image(load_image(image_file), width=250)
        st.text("Loading response....")
        st.write(pred(image_file))
main()