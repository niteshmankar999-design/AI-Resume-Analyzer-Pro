import streamlit as st

from resume_parser import extract_text
from skill_extractor import extract_skills
from resume_scorer import calculate_score
from matcher import calculate_match_score
from skill_gap import find_missing_skills
from recommendations import generate_recommendations
from report_generator import create_report
from keyword_analyzer import keyword_analysis

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #020617
    );
}

.main-title{
    text-align:center;
    font-size:3.2rem;
    font-weight:800;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #818cf8,
        #ec4899
    );
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:20px;
}

div[data-testid="metric-container"]{
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:18px;
    padding:15px;
}

.skill-tag{
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:8px 14px;
    border-radius:20px;
    margin:4px;
    font-size:14px;
}

.stDownloadButton button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Career Assistant")

    st.markdown("---")

    st.success("Features")

    st.write("✅ Resume Parsing")
    st.write("✅ ATS Score")
    st.write("✅ Job Matching")
    st.write("✅ Skill Gap Analysis")
    st.write("✅ ATS Keyword Coverage")
    st.write("✅ PDF Report")

    st.markdown("---")

    st.info("Version 2.0")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    "<h1 class='main-title'>🚀 AI Resume Analyzer Pro</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>AI Powered Resume Analysis, ATS Optimization and Job Matching Platform</p>",
    unsafe_allow_html=True
)

# --------------------------------------------------
# INPUTS
# --------------------------------------------------

job_description = st.text_area(
    "📋 Paste Job Description",
    height=220
)

uploaded_file = st.file_uploader(
    "📄 Upload Resume (PDF)",
    type=["pdf"]
)

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    score = calculate_score(
        text,
        skills
    )

    match_score = None
    missing_skills = []

    matched_keywords = []
    missing_keywords = []
    keyword_coverage = 0

    if job_description.strip():

        match_score = calculate_match_score(
            text,
            job_description
        )

        missing_skills = find_missing_skills(
            text,
            job_description
        )

        (
            matched_keywords,
            missing_keywords,
            keyword_coverage
        ) = keyword_analysis(
            text,
            job_description
        )

    # --------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📊 ATS Score",
            f"{score}/100"
        )

    with col2:
        st.metric(
            "🛠 Skills",
            len(skills)
        )

    with col3:
        if match_score is not None:
            st.metric(
                "🎯 Match",
                f"{match_score}%"
            )

    with col4:
        st.metric(
            "🔑 ATS Keywords",
            f"{keyword_coverage}%"
        )

    st.divider()

    # --------------------------------------------------
    # ATS SCORE
    # --------------------------------------------------

    st.subheader("📊 ATS Resume Score")

    st.progress(score)

    if score >= 80:
        st.success("🚀 Excellent Resume")
    elif score >= 60:
        st.info("👍 Good Resume")
    else:
        st.warning("⚠ Resume Needs Improvement")

    # --------------------------------------------------
    # SKILLS
    # --------------------------------------------------

    st.subheader("🎯 Detected Skills")

    skills_html = ""

    for skill in skills:
        skills_html += f"""
        <span class="skill-tag">{skill}</span>
        """

    st.markdown(
        skills_html,
        unsafe_allow_html=True
    )

    # --------------------------------------------------
    # MATCH ANALYSIS
    # --------------------------------------------------

    if match_score is not None:

        st.divider()

        st.subheader("🎯 Job Match Score")

        st.progress(int(match_score))

        if match_score >= 80:
            st.success("🔥 Excellent Match")
            st.balloons()

        elif match_score >= 60:
            st.info("👍 Good Match")

        else:
            st.warning("⚠ Low Match Score")

        # --------------------------------------------

        st.subheader("⚠ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.error(skill)

        else:
            st.success(
                "No missing skills detected!"
            )

        # --------------------------------------------

        st.subheader("🔑 ATS Keyword Coverage")

        st.progress(int(keyword_coverage))

        c1, c2 = st.columns(2)

        with c1:

            st.success("Matched Keywords")

            for keyword in matched_keywords:
                st.write(f"✅ {keyword}")

        with c2:

            st.warning("Missing Keywords")

            for keyword in missing_keywords:
                st.write(f"❌ {keyword}")

        # --------------------------------------------

        recommendations = generate_recommendations(
            score,
            missing_skills
        )

        st.subheader("💡 Recommendations")

        for rec in recommendations:
            st.info(rec)

        # --------------------------------------------
        # PDF REPORT
        # --------------------------------------------

        report_file = create_report(
            score,
            skills,
            match_score,
            missing_skills,
            recommendations
        )

        with open(report_file, "rb") as file:

            st.download_button(
                "📥 Download PDF Report",
                data=file,
                file_name="Resume_Analysis_Report.pdf",
                mime="application/pdf"
            )

    # --------------------------------------------------
    # RESUME TEXT
    # --------------------------------------------------

    with st.expander(
        "📄 View Extracted Resume Text"
    ):

        st.text_area(
            "Resume Content",
            text,
            height=400
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
    """
    <center>
    Made with ❤️ by Nitesh Mankar
    <br>
    AI Resume Analyzer Pro
    </center>
    """,
    unsafe_allow_html=True
)