import streamlit as st
from components.cards import project_card, experience_card, skill_tags

def render_home(data, images):
    st.markdown(f"""
    <div class="hero">
        <h1 class="gradient-title">{data['personal']['name']}</h1>
        <h3>{data['personal']['title']} — {data['personal']['location']}</h3>
        <p>
            <a href="{data['personal']['linkedin']}" target="_blank">LinkedIn</a> • 
            <a href="{data['personal']['github']}" target="_blank">GitHub</a> • 
            {data['personal']['email']}
        </p>
        <p>{data['summary']}</p>
    </div>
    <div class="card">
        <img src="data:image/png;base64,{images['home']}" class="card-image">
    </div>
    """, unsafe_allow_html=True)

def render_projects(data, images):
    st.subheader("💻 Projects")
    featured = [p for p in data['projects'] if p.get('featured')]
    others = [p for p in data['projects'] if not p.get('featured')]
    all_projects = featured + others
    cols = st.columns(3)
    for i, proj in enumerate(all_projects):
        with cols[i % 3]:
            img_key = proj.get('image', 'project1.png')
            img_b64 = images.get(img_key, images.get('project1.png', ''))
            project_card(proj, img_b64)

def render_skills(data, images):
    st.subheader("🛠 Skills")
    st.markdown(f'<img src="data:image/png;base64,{images["skills"]}" class="card-image" style="max-height:150px;">', unsafe_allow_html=True)
    skill_tags(data['skills'])

def render_experience(data, images):
    st.subheader("💼 Experience")
    for exp in data['experience']:
        img_b64 = images.get(exp['image'], '')
        experience_card(exp, img_b64)

def render_education(data, images):
    st.subheader("📚 Education")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['education']}" class="card-image">
        <p>{data['education']}</p>
    </div>
    """, unsafe_allow_html=True)

def render_certifications(data, images):
    st.subheader("📜 Certifications")
    cert_html = '<div class="card">'
    cert_html += f'<img src="data:image/png;base64,{images["certifications"]}" class="card-image">'
    for cert in data['certifications']:
        if isinstance(cert, dict):
            cert_html += f'<p>✅ <a href="{cert["url"]}" target="_blank">{cert["name"]}</a></p>'
        else:
            cert_html += f'<p>✅ {cert}</p>'
    cert_html += '</div>'
    st.markdown(cert_html, unsafe_allow_html=True)

def render_socials(data, images):
    st.subheader("🌐 Connect with Me")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['socials']}" class="card-image">
        <p><a href="{data['personal']['linkedin']}" target="_blank">LinkedIn</a></p>
        <p><a href="{data['personal']['github']}" target="_blank">GitHub</a></p>
        <p>✉️ {data['personal']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

def render_resume(data, images, resume_pdf_path):
    st.subheader("📄 My resume")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['resume']}" class="card-image">
    </div>
    """, unsafe_allow_html=True)
    try:
        with open(resume_pdf_path, "rb") as f:
            resume_bytes = f.read()
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=resume_bytes,
            file_name="Shailendra_resume.pdf",
            mime="application/pdf"
        )
    except FileNotFoundError:
        st.error("Resume PDF not found at resume/Shailendra_resume.pdf")
