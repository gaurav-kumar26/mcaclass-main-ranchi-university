
import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.webcam_input import reset_student_face_login


def login_screen():

    header_home()

    style_background_home()

    style_base_layout()

    # Go Back to Home Button Styling - Fixed Bottom Right
    st.markdown(
    """
    <style>
        /* Fixed top-right position */
        div.st-key-login_page_back_home {
            position: fixed !important;
            top: 125px !important;
            right: 30px !important;
            bottom: auto !important;
            z-index: 99999 !important;
            width: auto !important;
        }

        div.st-key-login_page_back_home button {
            background-color: #ed3da0 !important;
            color: white !important;
            border: none !important;
            border-radius: 35px !important;
            padding: 12px 28px !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            width: auto !important;
            transition: transform 0.25s ease,
                        filter 0.25s ease,
                        box-shadow 0.25s ease !important;
        }

        div.st-key-login_page_back_home button:hover {
            filter: brightness(1.08);
            transform: scale(1.05);
            box-shadow: 0 6px 16px rgba(237, 61, 160, 0.35);
        }

        @media (max-width: 768px) {
            div.st-key-login_page_back_home {
                top: 115px !important;
                right: 12px !important;
            }

            div.st-key-login_page_back_home button {
                padding: 9px 16px !important;
                font-size: 13px !important;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    # Go Back to Home Button
    if st.button(
        "← Go Back to Home",
        key="login_page_back_home"
    ):
        st.session_state["login_type"] = None
        st.session_state["page"] = "landing"
        st.rerun()

    # Student and Teacher Portal Cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")

        st.image(
            "https://i.ibb.co/844D9Lrt/mascot-student.png",
            width=120
        )

        if st.button(
            "Student Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right"
        ):
            reset_student_face_login()
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I'm Teacher")

        st.image(
            "https://i.ibb.co/CsmQQV6X/mascot-student.png",
            width=145
        )

        if st.button(
            "Teacher Portal",
            type="primary",
            icon=":material/arrow_outward:",
            icon_position="right"
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    # Footer
    footer_home()
