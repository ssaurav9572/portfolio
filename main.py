import streamlit as st
from base64 import b64encode
import os

def web_portfolio():
    # Page configuration
    st.set_page_config(page_title="Shailendra Saurav's Portfolio", page_icon="⭐")

    # Title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Shailendra Saurav</span>👋
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<style>div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)

    # Set the path to files
    base_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_path, "dp.png")
    pdf_path = os.path.join(base_path, "profile.pdf")

    # Load Profile Image
    try:
        with open(image_path, "rb") as img_file:
            img = "data:image/png;base64," + b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error("Profile image not found.")
        img = ""

    # Load Profile PDF
    try:
        with open(pdf_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
    except FileNotFoundError:
        st.error("Profile PDF not found.")
        pdf_bytes = None

    # Display Profile Image with Animation
    st.write(f"""
    <style>
    @keyframes slowTilt {{
        0%, 100% {{
            transform: rotate(0deg);
        }}
        50% {{
            transform: rotate(5deg);
        }}
    }}
    .box img {{
        width: 300px;
        height: 200px;
        border-radius: 50%;
        animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
        <div class="box">
            <img src="{img}">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Subtitle
    st.write(f"""
    <div class="subtitle" style="text-align: center;">Python Developer</div>
    """, unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        "LinkedIn": ["https://www.linkedin.com/in/ssaurav9572", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "GitHub": ["https://github.com/ssaurav9572", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    }

    social_icons_html = [
        f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
        f" style='width: 25px; height: 25px;'></a>"
        for platform in social_icons_data
    ]
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>
    """, unsafe_allow_html=True)

    # About Me Section
    st.subheader("About Me")
    st.markdown("""
    - 🧑‍💻 I am a **Python Developer** at [Cuebo.ai](https://cuebo.ai/), where I am currently working on a Voice Simulator project.
    - 🚀 Previously, I served as a Backend Developer Intern at [ethan.ai](https://www.ethan-ai.com/).
    - ❤️ I am passionate about *Artificial Intelligence, Software Engineering, Data Analytics, Data Engineering, Automation*, and more!
    - 🤖 Additionally, I have also worked as an intern at [Wiley Edge](https://wileyedge.neohire.io/)
    - 🏂 In my free time, I enjoy practicing sports such as Cricket and Cycling.
    - 🪧 You can reach me at ssaurav9572@gmail.com.
    - 🏠 Based in India.
    """)

    # Download CV button
    if pdf_bytes:
        st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="profile.pdf", mime="application/pdf")
    else:
        st.warning("CV file not available for download.")

    st.write(f"""
    <div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()
