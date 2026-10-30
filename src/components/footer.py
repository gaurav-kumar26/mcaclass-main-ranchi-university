import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/bMyV8RgR/gaurav-kumar-logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; padding:1.75rem 1rem; display:flex; gap:8px; justify-content:center; align-items:center; flex-wrap:wrap; background:#5865F2; width:100%;">
        <p style="font-weight:bold; color:white; margin:0;"> Created with 👨🏻‍💻 by </p>
        <img src='{logo_url}' alt="Gaurav Kumar" style="max-height:25px;" />
        </div>
                """, unsafe_allow_html=True)
    
def footer_dashboard():
    logo_url = "https://i.ibb.co/bMyV8RgR/gaurav-kumar-logo.png"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; item-align:center">
        <p style="font-weight:bold; color:black;"> Created with 👨🏻‍💻 by </p>
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                """, unsafe_allow_html=True)
