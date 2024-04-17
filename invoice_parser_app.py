import os
import json
import streamlit as st
from PIL import Image

# Function to load images from a directory
def load_images_from_dir(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            images.append(os.path.join(directory, filename))
    return images

# Function to load text from a directory
def load_text_from_dir(directory):
    texts = {}
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), "r") as file:
                texts[filename[:-4]] = file.read()
    return texts

# Function to load annotations from a directory
def load_annotations_from_dir(directory):
    annotations = {}
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                annotations[filename[:-5]] = json.load(file)
    return annotations

# Load images, text, and annotations from the test set directory
test_set_images = load_images_from_dir("test_set/images")
test_set_texts = load_text_from_dir("test_set/text")
test_set_annotations = load_annotations_from_dir("test_set/annotations")

# Streamlit app
st.title("Invoice Extractor")

# Display images horizontally
st.image(test_set_images, width=200)

# Select an image
selected_image = st.selectbox("Select an image:", test_set_images)

# Display selected image
st.image(selected_image, use_column_width=True)

# Display corresponding text and annotations
selected_filename = os.path.splitext(os.path.basename(selected_image))[0]
if selected_filename in test_set_texts:
    st.write("Text Content:")
    st.text(test_set_texts[selected_filename])
if selected_filename in test_set_annotations:
    st.write("Annotations:")
    st.json(test_set_annotations[selected_filename])

# Main function to run the Streamlit app
if __name__ == "__main__":
    st.run()
