import base64
import os
import streamlit as st

@st.cache_data(ttl=3600)
def get_base64(image_path):
    """Return base64 encoded string of image file. If not found, return a tiny placeholder."""
    try:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAC1wG/2k0lZQAAAABJRU5ErkJggg=="

def load_image(image_name, base_dir):
    """Given an image filename, return base64 string."""
    path = os.path.join(base_dir, "images", image_name)
    return get_base64(path)
