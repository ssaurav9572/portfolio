import streamlit as st
import json
import os
from utils.image_loader import load_image
from components import sections

# --- Page config ---
st.set_page_config(page_title="Shailendra Saurav | Portfolio", layout="wide")

# --- Base directory ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Load custom CSS ---
with open(os.path.join(BASE_DIR, "assets", "styles.css")) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Load data from JSON with caching ---
@st.cache_data
def load_resume_data():
    json_path = os.path.join(BASE_DIR, "data", "resume.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

data = load_resume_data()

# --- Load all images with caching ---
@st.cache_data(ttl=3600)
def load_all_images(base_dir, image_map):
    """Convert all image filenames to base64 strings."""
    images = {}
    for key, filename in image_map.items():
        if isinstance(filename, list):
            # For list of images (projects/experience), we load individually later
            continue
        images[key] = load_image(filename, base_dir)
    return images

# Build image mapping from JSON
image_map = data.get("images", {})
# Also include project images (they are in project entries)
project_images = {}
for proj in data["projects"]:
    if "image" in proj and proj["image"] not in project_images:
        project_images[proj["image"]] = load_image(proj["image"], BASE_DIR)
# Experience images
exp_images = {}
for exp in data["experience"]:
    if "image" in exp and exp["image"] not in exp_images:
        exp_images[exp["image"]] = load_image(exp["image"], BASE_DIR)

# Merge all into one dict for easy access
all_images = load_all_images(BASE_DIR, image_map)
all_images.update(project_images)
all_images.update(exp_images)

# --- Sidebar navigation ---
st.sidebar.title("📂 Sections")
section = st.sidebar.radio("Navigate to:", 
    ["Home", "Projects", "Skills", "Experience", "Education", "Certifications", "Socials", "Resume"])

# --- Render selected section ---
if section == "Home":
    sections.render_home(data, all_images)

elif section == "Projects":
    sections.render_projects(data, all_images)

elif section == "Skills":
    sections.render_skills(data, all_images)

elif section == "Experience":
    sections.render_experience(data, all_images)

elif section == "Education":
    sections.render_education(data, all_images)

elif section == "Certifications":
    sections.render_certifications(data, all_images)

elif section == "Socials":
    sections.render_socials(data, all_images)

elif section == "Resume":
    resume_pdf = os.path.join(BASE_DIR, "resume", "Shailendra_resume.pdf")
    sections.render_resume(data, all_images, resume_pdf)

# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer">Made with ❤️ by Shailendra Saurav — <strong>This portfolio was crafted with ChatGPT</strong></div>', unsafe_allow_html=True)