# netflix_portfolio_streamlit.py
import streamlit as st
import base64
import os

# get script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(page_title="Shailendra Saurav | Portfolio", layout="wide")

# --- Custom CSS (Gradient Background + Fancy Sidebar + Cards) ---
st.markdown("""
<style>
/* Soft text colors for readability */
.stApp, section[data-testid="stSidebar"] {
    font-family: 'Montserrat', sans-serif !important;
    color: #f0f0f5 !important;  /* soft white */
    text-shadow: 1px 1px 3px rgba(0,0,0,0.6); /* subtle shadow for contrast */
}

/* Header */
.header {
    padding: 30px;
    text-align: center;
    background: rgba(0,0,0,0.5);
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.6);
    font-family: 'Roboto Slab', serif;
    color: #f0f0f5;
    text-shadow: 2px 2px 5px rgba(0,0,0,0.6);
}

/* Card style */
.card {
    background: rgba(255,255,255,0.12);  /* slightly stronger card opacity */
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    transition: transform 0.2s ease-in-out;
    font-family: 'Montserrat', sans-serif;
    color: #f0f0f5;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
}
.card:hover {
    transform: scale(1.03);
    background: rgba(255,255,255,0.18);
}

/* Headings */
h1, h2, h3, h4, h5, h6 {
    color: #f8f8ff !important;  /* slightly off-white */
    font-weight: 800 !important;
    font-family: 'Roboto Slab', serif !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.6);
}

/* Links */
a {
    color: #00E5FF;
    font-weight: bold;
    text-decoration: none;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}
a:hover {
    color: #ffcc70;
    text-decoration: underline;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: #ffffff !important;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    padding: 0.5em 1.2em;
    cursor: pointer;
    font-family: 'Montserrat', sans-serif;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #ff512f, #dd2476);
}

/* Footer */
.footer {
    color: #e0e0e0;
    text-align: center;
    padding: 20px;
    font-size: 14px;
    opacity: 0.9;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
}
</style>
""", unsafe_allow_html=True)


# --- Backgrounds for sections ---
backgrounds = {
    "home": os.path.join("images", "shailendra_zensar.jpg"),
    "projects": os.path.join("images", "project.png"),
    "skills": os.path.join("images", "skills.png"),
    "education": os.path.join("images", "college.png"),
    "certifications": os.path.join("images", "certificate.png"),
    "Socials": os.path.join("images", "github.png"),
    "experience": [
        os.path.join("images", "zensar.png"),
        os.path.join("images", "wileyedge.png"),
        os.path.join("images", "cueboai.png"),
        os.path.join("images", "ethanai.png")
    ]
}

# --- Helper: set background dynamically ---
def set_background(image_file):
    st.markdown(f"""
    <style>
    .stApp {{
    background: none !important;
    color: #f5f5f5 !important;
    font-weight: 600 !important;
    font-size: 16px !important;}}
    /* Background image only for main page, not sidebar */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: url('data:image/png;base64,{image_file}') no-repeat center center fixed;
        background-size: cover;
        opacity: 0.25;
        z-index: -2;
    }}

    /* Dark overlay for readability */
    .stApp::after {{
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: -1;
    }}

    /* Sidebar solid */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #141E30, #243B55) !important;
        color: white !important;
        border-radius: 12px;
        padding: 20px;
        opacity: 1 !important;
    }}
    section[data-testid="stSidebar"] * {{
        color: #ffffff !important;
        font-weight: 700 !important;  /* bold sidebar text */
        font-size: 15px !important;
    }}

    /* Headings bigger & brighter */
    h1, h2, h3, h4, h5, h6 {{
        color: #ffffff !important;
        font-weight: 800 !important;
    }}
    </style>
    """, unsafe_allow_html=True)



def get_base64(file_name):
    file_path = os.path.join(BASE_DIR, file_name)
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


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
         "website": "https://stockanalysisdashboards.streamlit.app/"},

        {"title": "News Aggregator", "desc": "Consolidates data from multiple APIs to deliver up-to-date news.", 
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
    ["Home", "Projects", "Skills", "Experience", "Education", "Certifications", "Socials"])

# --- Sections ---
if section == "Home":
    bg_image = get_base64(backgrounds["home"])
    set_background(bg_image)
    st.markdown(f"""
    <div class="overlay">
        <h1>🎬 {resume['name']}</h1>
        <h3>{resume['title']} — {resume['contact']['location']}</h3>
        <p><a href="{resume['links']['linkedin']}" target="_blank">LinkedIn</a> • 
           <a href="{resume['links']['github']}" target="_blank">GitHub</a> • 
           {resume['contact']['email']}</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Projects":
    bg_image = get_base64(backgrounds["projects"])
    set_background(bg_image)
    st.subheader("💻 Projects")
    
    for p in resume["projects"]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"#### {p['title']}")
        st.write(p["desc"])
        st.write(f"**Tech:** {p['tech']}")
        
        # GitHub link
        st.markdown(f"[🔗 View on GitHub]({p['link']})")
        
        # Optional website/live app link
        if "website" in p:
            st.markdown(f"[🌐 Try Live App]({p['website']})")
        
        st.markdown("</div>", unsafe_allow_html=True)


elif section == "Skills":
    bg_image = get_base64(backgrounds["skills"])
    set_background(bg_image)
    st.subheader("🛠 Skills")
    sk = resume["skills"]
    st.write("**Languages:** " + ", ".join(sk["languages"]))
    st.write("**Frameworks:** " + ", ".join(sk["frameworks"]))
    st.write("**Databases:** " + ", ".join(sk["databases"]))
    st.write("**Tools & Cloud:** " + ", ".join(sk["tools"] + sk["cloud"]))

elif section == "Experience":
    if "exp_index" not in st.session_state:
        st.session_state.exp_index = 0

    exp = resume["experience"][st.session_state.exp_index]
    bg_image = get_base64(backgrounds["experience"][st.session_state.exp_index])
    set_background(bg_image)

    st.markdown("<div class='overlay'>", unsafe_allow_html=True)
    st.markdown(f"### {exp['role']} — *{exp['company']}*")
    st.write(f"📅 {exp['duration']}")
    for b in exp["bullets"]:
        st.markdown(f"- {b}")
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅ Previous", disabled=st.session_state.exp_index == 0):
            st.session_state.exp_index = max(0, st.session_state.exp_index - 1)
    with col2:
        if st.button("Next ➡", disabled=st.session_state.exp_index == len(resume["experience"]) - 1):
            st.session_state.exp_index = min(len(resume["experience"]) - 1, st.session_state.exp_index + 1)

elif section == "Education":
    bg_image = get_base64(backgrounds["education"])
    set_background(bg_image)
    st.subheader("📚 Education")
    st.write("Bachelor of Engineering (B.E), Computer Science and Engineering — VTU (2018–2022)")


elif section == "Certifications":
    bg_image = get_base64(backgrounds["certifications"])
    set_background(bg_image)
    st.subheader("📜 Certifications")
    st.write("✅ Programming Foundations with JavaScript, HTML and CSS")  
    st.write("✅ Goldman Sachs Software Engineering Virtual Experience Program")  
    st.write("[✅ Programming for Everybody (Getting Started with Python)](https://www.coursera.org/account/accomplishments/verify/CZD6YU9S5EC7)")  

elif section == "Socials":
    bg_image = get_base64(backgrounds["Socials"])
    set_background(bg_image)
    st.subheader("🌐 Connect with Me")
    st.markdown(f"[LinkedIn]({resume['links']['linkedin']}) | [GitHub]({resume['links']['github']}) | ✉️ {resume['contact']['email']}")

# --- Footer ---
st.markdown("---")
st.markdown('<div class="footer">Made with ❤️ by Shailendra Saurav — <strong>This portfolio was crafted with ChatGPT</strong></div>', unsafe_allow_html=True)
