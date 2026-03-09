import streamlit as st

def project_card(project, img_base64):
    st.markdown(f"""
    <div class="card">
        <img src="data:image/png;base64,{img_base64}" class="card-image">
        <h4>{project['title']}</h4>
        <p>{project['desc']}</p>
        <p><strong>Tech:</strong> {', '.join(project['tech'])}</p>
        <p>
            <a href="{project['github']}" target="_blank">🔗 GitHub</a>
            {f' • <a href="{project["live"]}" target="_blank">🌐 Live</a>' if 'live' in project else ''}
        </p>
    </div>
    """, unsafe_allow_html=True)

def experience_card(exp, img_base64):
    bullets = "".join([f"<p>- {b}</p>" for b in exp['bullets']])
    st.markdown(f"""
    <div class="card timeline-item">
        <img src="data:image/png;base64,{img_base64}" class="card-image" style="max-height:100px;">
        <h3>{exp['role']} — <em>{exp['company']}</em></h3>
        <p>📅 {exp['duration']}</p>
        {bullets}
    </div>
    """, unsafe_allow_html=True)

def skill_tags(skills_dict):
    """Display skills as interactive tags."""
    html = ""
    for category, items in skills_dict.items():
        html += f"<p><strong>{category.title()}:</strong> "
        for skill in items:
            html += f'<span class="skill-tag">{skill}</span> '
        html += "</p>"
    st.markdown(html, unsafe_allow_html=True)