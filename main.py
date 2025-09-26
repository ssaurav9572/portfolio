import streamlit as st
import base64
import os

# Get script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="Shailendra Saurav | Portfolio", layout="wide")

# --- Custom CSS (Netflix-style Cards with Full Image Display and Visible Download Button) ---
st.markdown("""
<style>
/* General styling */
.stApp, section[data-testid="stSidebar"] {
    font-family: 'Montserrat', sans-serif !important;
    color: #f0f0f5 !important;
    background: #141414 !important; /* Netflix dark background */
}

/* Header */
.header {
    padding: 30px;
    text-align: center;
    background: rgba(0,0,0,0.7);
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.6);
    font-family: 'Roboto Slab', serif;
    color: #f0f0f5;
    margin-bottom: 20px;
}

/* Netflix-style Card */
.card {
    background: #1f1f1f !important; /* Darker card background */
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    overflow: hidden;
    position: relative;
    color: #f0f0f5;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.7);
}

/* Card Image */
.card-image {
    width: 100%;
    max-height: 200px; /* Maintain height limit but allow flexibility */
    object-fit: contain; /* Show full image without cropping */
    border-radius: 8px;
    margin-bottom: 10px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #ffffff !important;
    font-weight: 800 !important;
    font-family: 'Roboto Slab', serif !important;
}

/* Links */
a {
    color: #e50914; /* Netflix red */
    font-weight: bold;
    text-decoration: none;
}
a:hover {
    color: #ffcc70;
    text-decoration: underline;
}

/* Buttons */
div.stButton > button {
    background: #e50914; /* Netflix red */
    color: #ffffff !important;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 0.5em 1.2em;
    cursor: pointer;
    font-family: 'Montserrat', sans-serif;
}
div.stButton > button:hover {
    background: #b20710; /* Darker red */
}

/* Download Button Specific Styling */
div.stDownloadButton > button {
    background: #e50914 !important; /* Netflix red */
    color: #ffffff !important; /* Ensure text is white */
    font-weight: 600 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.5em 1.2em !important;
    cursor: pointer !important;
    font-family: 'Montserrat', sans-serif !important;
}
div.stDownloadButton > button:hover {
    background: #b20710 !important; /* Darker red */
}
div.stDownloadButton > button > span {
    color: #ffffff !important; /* Force inner text to white */
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #1f1f1f !important;
    color: #ffffff !important;
    border-radius: 12px;
    padding: 20px;
}
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 15px !important;
}

/* Footer */
.footer {
    color: #b3b3b3;
    text-align: center;
    padding: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# --- Helper: Convert image file to base64 ---
def get_base64(file_name):
    file_path = os.path.join(BASE_DIR, "images", file_name)
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        # Fallback to a placeholder image if file not found
        return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAC1wG/2k0lZQAAAABJRU5ErkJggg=="

# --- Images mapping ---
images = {
    "home": get_base64("shailendra_zensar.jpg"),
    "projects": [
        get_base64("project1.png"),
        get_base64("project2.png")
    ],
    "skills": get_base64("skills.png"),
    "education": get_base64("college.png"),
    "certifications": get_base64("certificate.png"),
    "Socials": get_base64("github.png"),
    "resume": get_base64("resume.png"),
    "experience": [
        get_base64("zensar.png"),
        get_base64("cueboai.png"),
        get_base64("ethanai.png"),
        get_base64("wileyedge.png")
    ]
}

# --- Resume Data ---
resume = {
    "name": "Shailendra Saurav",
    "title": "Data Engineer | Backend Developer",
    "contact": {"email": "ssaurav9572@gmail.com", "location": "Dhanbad, Jharkhand"},
    "links": {
        "linkedin": "https://www.linkedin.com/in/ssaurav9572",
        "github": "https://github.com/ssaurav9572"
    },
    "summary": (
        "Data Engineer with experience in backend development, data engineering, and cloud automation. "
        "Skilled in Python, Django, Microsoft Fabric, AWS Redshift, and Terraform. Strong in building ETL "
        "pipelines, API development, and deploying scalable cloud infrastructure on AWS and Azure."
    ),
    "projects": [
        {"title": "Stock Market Dashboard", 
         "desc": "Interactive tool for analyzing 5 years of historical stock data.",
         "tech": "Python, Streamlit, Pandas, Plotly", 
         "link": "https://github.com/ssaurav9572/stock_market_dashboard", 
         "website": "https://stockanalysisbyshailu.streamlit.app/"},
        {"title": "News Aggregator", 
         "desc": "Consolidates data from multiple APIs to deliver up-to-date news.", 
         "tech": "Python, BeautifulSoup, Requests", 
         "link": "https://github.com/ssaurav9572/news-aggregator"}
    ],
    "skills": {
        "languages": ["Python", "C", "C++"],
        "frameworks": ["Django", "Flask", "Streamlit", "Terraform"],
        "databases": ["MySQL", "PostgreSQL", "SQL"],
        "tools": ["Docker", "Git", "PowerBI"],
        "cloud": ["Azure", "Microsoft Fabric"]
    },
    "experience": [
        {
            "role": "Junior Software Engineer",
            "company": "Zensar Technologies",
            "duration": "Dec 2024 – Present",
            "bullets": [
                "Migrated and optimized MS Fabric procedures into AWS Redshift stored procedures, improving query efficiency and reducing processing time.",
                "Designed and implemented a data engineering project on Blinkit dataset using Azure Blob + GitHub with Medallion Architecture (Bronze, Silver, Gold).",
                "Deployed and managed Microsoft Fabric infra components (Resource Groups, Firewalls, Gateways, Key Vaults).",
                "Automated infrastructure provisioning using Terraform CLI."
            ]
        },
        {
            "role": "Python Developer Intern",
            "company": "Cuebo.ai",
            "duration": "Aug 2024 – Nov 2024",
            "bullets": [
                "Streamlined RESTful API development in Django to deliver new features and improve user interaction.",
                "Automated AWS workflows using Step Functions and EventBridge (via boto3).",
                "Optimized model performance using prompt engineering (few-shot, zero-shot).",
                "Developed call categorization features mapped with Django models.",
                "Analyzed system performance and refined prompt behaviors."
            ]
        },
        {
            "role": "Backend Developer Intern",
            "company": "ethan.ai",
            "duration": "Feb 2024 – Apr 2024",
            "bullets": [
                "Built robust APIs using Python and Django.",
                "Developed and tested web apps with Streamlit.",
                "Performed API testing with Postman.",
                "Implemented unit tests to improve code quality.",
                "Maintained Git repositories for version control."
            ]
        },
        {
            "role": "Intern",
            "company": "Wiley Edge",
            "duration": "Oct 2022 – Mar 2023",
            "bullets": [
                "Collaborated in team projects, developing a Django-based application as part of SDLC.",
                "Trained in Python, SQL, and Linux, gaining expertise in debugging and optimization."
            ]
        }
    ]
}

# --- Sidebar ---
st.sidebar.title("📂 Sections")
section = st.sidebar.radio("Navigate to:", 
    ["Home", "Projects", "Skills", "Experience", "Education", "Certifications", "Socials", "Resume"])

# --- Sections ---
if section == "Home":
    st.markdown(f"""
    <div class="header">
        <h1>🎬 {resume['name']}</h1>
        <h3>{resume['title']} — {resume['contact']['location']}</h3>
        <p><a href="{resume['links']['linkedin']}" target="_blank">LinkedIn</a> • 
           <a href="{resume['links']['github']}" target="_blank">GitHub</a> • 
           {resume['contact']['email']}</p>
        <p>{resume['summary']}</p>
    </div>
    <div class="card">
        <img src="data:image/png;base64,{images['home']}" class="card-image">
    </div>
    """, unsafe_allow_html=True)

elif section == "Projects":
    st.subheader("💻 Projects")
    cols = st.columns(2)  # Two-column layout for Netflix-style grid
    for i, p in enumerate(resume["projects"]):
        with cols[i % 2]:
            project_image = images['projects'][i]  # Use i-th image
            st.markdown(f"""
            <div class="card">
                <img src="data:image/png;base64,{project_image}" class="card-image">
                <h4>{p['title']}</h4>
                <p>{p['desc']}</p>
                <p><strong>Tech:</strong> {p['tech']}</p>
                <p><a href="{p['link']}" target="_blank">🔗 View on GitHub</a></p>
                {"<p><a href='" + p['website'] + "' target='_blank'>🌐 Try Live App</a></p>" if 'website' in p else ""}
            </div>
            """, unsafe_allow_html=True)

elif section == "Skills":
    st.subheader("🛠 Skills")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['skills']}" class="card-image">
        <p><strong>Languages:</strong> {', '.join(resume['skills']['languages'])}</p>
        <p><strong>Frameworks:</strong> {', '.join(resume['skills']['frameworks'])}</p>
        <p><strong>Databases:</strong> {', '.join(resume['skills']['databases'])}</p>
        <p><strong>Tools & Cloud:</strong> {', '.join(resume['skills']['tools'] + resume['skills']['cloud'])}</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Experience":
    st.subheader("💼 My Experience")
    if "exp_index" not in st.session_state:
        st.session_state.exp_index = 0

    exp = resume["experience"][st.session_state.exp_index]
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['experience'][st.session_state.exp_index]}" class="card-image">
        <h3>{exp['role']} — <em>{exp['company']}</em></h3>
        <p>📅 {exp['duration']}</p>
        {"".join([f"<p>- {b}</p>" for b in exp['bullets']])}
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ Previous", disabled=st.session_state.exp_index == 0):
            st.session_state.exp_index = max(0, st.session_state.exp_index - 1)
    with col2:
        if st.button("Next ➡", disabled=st.session_state.exp_index == len(resume["experience"]) - 1):
            st.session_state.exp_index = min(len(resume["experience"]) - 1, st.session_state.exp_index + 1)

elif section == "Education":
    st.subheader("📚 Education")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['education']}" class="card-image">
        <p>Bachelor of Engineering (B.E), Computer Science and Engineering — VTU (2018–2022)</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Certifications":
    st.subheader("📜 Certifications")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['certifications']}" class="card-image">
        <p>✅ Programming Foundations with JavaScript, HTML and CSS</p>
        <p>✅ Goldman Sachs Software Engineering Virtual Experience Program</p>
        <p><a href="https://www.coursera.org/account/accomplishments/verify/CZD6YU9S5EC7" target="_blank">✅ Programming for Everybody (Getting Started with Python)</a></p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Socials":
    st.subheader("🌐 Connect with Me")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['Socials']}" class="card-image">
        <p><a href="{resume['links']['linkedin']}" target="_blank">LinkedIn</a></p>
        <p><a href="{resume['links']['github']}" target="_blank">GitHub</a></p>
        <p>✉️ {resume['contact']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Resume":
    st.subheader("📄 My resume")
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{images['resume']}" class="card-image">
    </div>
    """, unsafe_allow_html=True)

    # Load resume PDF
    resume_pdf_path = os.path.join(BASE_DIR, "resume", "Shailendra_resume.pdf")
    try:
        with open(resume_pdf_path, "rb") as f:
            resume_bytes = f.read()
    except FileNotFoundError:
        resume_bytes = None
        st.error("Resume PDF not found at portfolio/resume/Shailendra_resume.pdf")

    if resume_bytes:
        st.download_button(
            label="📥 Download Resume (PDF)",
            data=resume_bytes,
            file_name="Shailendra_resume.pdf",
            mime="application/pdf"
        )

# --- Footer ---
st.markdown("---")

st.markdown('<div class="footer">Made with ❤️ by Shailendra Saurav — <strong>This portfolio was crafted with ChatGPT</strong></div>', unsafe_allow_html=True)

