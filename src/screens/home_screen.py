import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

from src.components.footer import footer_home

LOGO_URL = "https://i.ibb.co/YTYGn5qV/logo.png"
STUDENT_URL = "https://i.ibb.co/844D9Lrt/mascot-student.png"

STATIC_ROOT = Path(__file__).resolve().parents[2] / "static"


def _file_to_data_uri(path: Path) -> str:
    suffix = path.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
        ".gif": "image/gif",
    }.get(suffix, "application/octet-stream")
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _resolve_asset(*relative_names: str, fallback: str) -> str:
    search_dirs = [
        STATIC_ROOT / "img",
        STATIC_ROOT / "img" / "demo",
    ]
    for name in relative_names:
        for folder in search_dirs:
            candidate = folder / name
            if candidate.is_file():
                return _file_to_data_uri(candidate)
    return fallback


def _render_html(markup: str) -> None:
    st.html(dedent(markup).strip())


def _open_portal():
    st.session_state["page"] = "portal"
    st.rerun()


def _consume_portal_query():
    if st.query_params.get("nav") != "portal":
        return

    join_code = st.query_params.get("join-code")
    st.query_params.clear()
    if join_code:
        st.query_params["join-code"] = join_code
    _open_portal()


def _inject_styles():
    css_path = STATIC_ROOT / "css" / "style.css"
    if css_path.is_file():
        st.html(css_path)


def home_screen():
    _consume_portal_query()
    _inject_styles()

    logo = _resolve_asset("logo.png", "mca-logo.png", fallback=LOGO_URL)
    student_photo = _resolve_asset(
        "student.png",
        "profile.png",
        "mascot-student.png",
        fallback=STUDENT_URL,
    )
    attendance_shot = _resolve_asset(
        "attendance.png",
        "attendance-screenshot.png",
        "demo-attendance.png",
        fallback="",
    )

    attendance_media = (
        f'<div class="att-shot"><img src="{attendance_shot}" alt="Attendance screenshot"></div>'
        if attendance_shot
        else ""
    )

    nav_left, nav_center, nav_right = st.columns([1.4, 3.2, 1.2], vertical_alignment="center")
    with nav_left:
        _render_html(
            f"""
            <div class="logo mca-navbar-marker">
                <img src="{logo}" alt="MCA CLASS logo">
                <span class="logo-text">MCA<br>CLASS</span>
            </div>
            """
        )
    with nav_center:
        _render_html(
            """
            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#features">Features</a>
                <a href="#technology">Tech Stack</a>
            </div>
            """
        )
    with nav_right:
        if st.button("Login →", key="landing_nav_login"):
            _open_portal()

    left, center, right = st.columns([1, 1.7, 1], vertical_alignment="center", gap="medium")
    with left:
        _render_html(
            f"""
            <div class="floating-card card-left" id="home">
                <div class="att-preview">
                    <h4>📋 Take Attendance</h4>
                    <div class="att-table">
                        <b>Attendance Report</b><br>
                        Gaurav Kumar &nbsp; 🟢 Present<br>
                        Kumkum Kumari &nbsp; 🟢 Present<br>
                        Kushal Bhadra &nbsp; 🟢 Present<br>
                        Roushan Kumar &nbsp; 🔴 Absent
                    </div>
                    {attendance_media}
                    <div class="att-actions">
                        <span>Upload Photos</span>
                        <span>Face Analysis</span>
                    </div>
                </div>
            </div>
            """
        )
    with center:
        _render_html(
            """
            <div class="hero-copy">
                <div class="badge">Welcome to MCA CLASS</div>
                <h1>
                    AI Powered<br>
                    Attendance<br>
                    <span>System</span>
                </h1>
                <p>
                    Revolutionizing the classroom with next-gen computer vision
                    and voice biometrics. Trusted by educators for speed, accuracy,
                    and security.
                </p>
            </div>
            """
        )
        action_left, action_right = st.columns([1.05, 1.2], vertical_alignment="center")
        with action_left:
            if st.button("Login →", key="landing_hero_login"):
                _open_portal()
        with action_right:
            _render_html(
                """
                <a class="link-action" href="#features">Explore Features →</a>
                """
            )
    with right:
        _render_html(
            f"""
            <div class="floating-card card-right">
                <div class="profile-inner">
                    <img src="{logo}" alt="" style="height:42px;width:auto;aspect-ratio:auto;background:transparent;">
                    <h3>MCA CLASS</h3>
                    <p>SMART ATTENDANCE</p>
                    <div class="profile-photo">
                        <img src="{student_photo}" alt="Student profile">
                    </div>
                </div>
            </div>
            """
        )

    _render_html(
        """
        <section class="features" id="features">
            <h2>Powerful Features</h2>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="f-icon-box">📸</div>
                    <h3>Face Recognition</h3>
                    <p>AI-powered facial recognition for identifying enrolled students.</p>
                </div>
                <div class="feature-card">
                    <div class="f-icon-box">🎤</div>
                    <h3>Voice Recognition</h3>
                    <p>Voice-based student identification using voice embeddings.</p>
                </div>
                <div class="feature-card">
                    <div class="f-icon-box">📊</div>
                    <h3>Automated Attendance</h3>
                    <p>Automatic attendance processing, confirmation and database storage.</p>
                </div>
            </div>
        </section>
        """
    )

    _render_html(
        """
        <section class="tech-stack" id="technology">
            <p class="section-tag">TECHNOLOGY STACK</p>
            <h2>Built With Modern Tools</h2>
            <div class="tech-grid">
                <div class="tech-card"><div class="t-icon">🐍</div><h4>Python</h4><p>Core language for AI pipelines</p></div>
                <div class="tech-card"><div class="t-icon">⚡</div><h4>Streamlit</h4><p>Interactive classroom web app</p></div>
                <div class="tech-card"><div class="t-icon">😊</div><h4>dlib</h4><p>Face detection and landmarks</p></div>
                <div class="tech-card"><div class="t-icon">🔢</div><h4>NumPy</h4><p>Fast numerical processing</p></div>
                <div class="tech-card"><div class="t-icon">🎧</div><h4>Librosa</h4><p>Audio feature extraction</p></div>
                <div class="tech-card"><div class="t-icon">🗣️</div><h4>Resemblyzer</h4><p>Voice biometric embeddings</p></div>
                <div class="tech-card"><div class="t-icon">🧠</div><h4>Scikit-learn</h4><p>Recognition classifiers</p></div>
                <div class="tech-card"><div class="t-icon">🗄️</div><h4>Supabase</h4><p>Auth-ready cloud database</p></div>
            </div>
        </section>
        """
    )

    footer_home()
