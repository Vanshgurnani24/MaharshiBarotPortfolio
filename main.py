import streamlit as st
import pathlib

def load_css(file_path: str):
    with open(file_path, 'r') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS file
css_file=pathlib.Path("assets/style.css")
load_css(css_file)


hide_st_style="""
    <style>
    #MainMenu{
    visibility:hidden;
    }
    footer {
        visibility:hidden;
    }
    </style>
"""
st.html(hide_st_style)

about_me=st.Page(
    page="others/about.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
earzz=st.Page(
    page="others/earzz.py",
    title="Earzz",
    icon=":material/headphones:"
)
CMS=st.Page(
    page='others/CMS.py',
    title="Canteen Management System",
    icon=":material/restaurant:"
)
MHM=st.Page(
    page='others/MHM.py',
    title="Mental Health Management System",
    icon=":material/medication:"
)
Speak_for_speechless=st.Page(
    page='others/NGO.py',
    title='Speak for Speechless',
    icon=":material/cruelty_free:"
)
pg=st.navigation(
    {
        "About Me":[about_me],
        "Work":[earzz,CMS,MHM],
        "Other Works":[Speak_for_speechless]
    }

)


st.sidebar.text("Developed with ♥ by Vansh")


pg.run()