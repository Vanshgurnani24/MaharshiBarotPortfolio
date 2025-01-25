import streamlit as st

class MentalHealthManagement:
    def __init__(self):
        st.header(":red[About MHM :material/local_hospital:]",divider='red',anchor=False)
        col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
        with col1:
            st.html("""<p class='mhm-descritpion'>
                    This project have system for monitoring and supporting the mental health of children. It involves tailored surveillance, specialized assessment tools, and a dynamic tracking platform. By amalgamating data from diverse sources and employing technology-driven solutions, the project aims to provide timely interventions and foster a supportive environment for children's mental well-being
                </p>""")
        with col2:
            st.subheader(":red[This project is still under development :material/construction:]",anchor=False)
    
    def keyfeatures(self):
        st.header(":grey[Key Features :material/key:]",anchor=False,divider='grey')
        st.write("""
        - :grey[Appointment Booking]
        - :grey[Therapists and Patients Registration]
        - :grey[Analysis of Patients]
        - :grey[Report generation of Analysis]
        """)
    def Benefits(self):
        st.header(":green[Benefits :material/loyalty:]",divider='green',anchor=False)
        st.write("""
        - :green[Better communication]
        - :green[Reduced stigma]
        - :green[Enhanced patient care]
        - :green[Care coordination]
        - :green[Improved emergency response]
        - :green[Streamlined workflows]
        - :green[Transparency]
        """)
    def ProjectMedia(self):
        st.header(":violet[Project Media :material/tactic:]",anchor=False,divider='violet')
        with st.expander("Project Media :material/play_arrow:"):
            st.video("assets/Videos/MHM video.mp4",autoplay=True,muted=True,loop=True)
            st.write("""
                - :violet[Note: This project is still under development and has not yet been deployed to GitHub. Once completed, it will be available for download and use on GitHub.]
            """)
    def TeamMembers(self):
        st.header(":orange[Project Team Members :material/groups:]",anchor=False,divider='orange')
        col1,col2=st.columns(2,gap='large',vertical_alignment='center')
        with col1:
            st.title("VANSH GURNANI",anchor=False)
            st.write("""
            A computer engineering student passionate about data science, building a network of astute minds to cultivate teamwork and growth.
            """)
        with col2:
            st.image(image="assets/Photos/VANSH GURNANI.png",use_container_width=True)
        
        st.subheader(":blue[Technology Proficiency]",divider='blue',anchor=False)
        st.write("""
        - :blue[Technologies: Frontend Developer, Backend Developer, CRUD Developer.]
        - :blue[Programming: Python, SQL, HTML, CSS,C,C++.]
        - :blue[Frameworks: Pandas, Numpy, Matplotlib, Seaborn, Scikit, Streamlit, Flask.]
        - :blue[Data Visualization: MS Excel, PowerBi, Plotly.]
        - :blue[Video Editing: Adobe Premiere pro, Adobe After Effects, Wondershare Filmora, Sony Vegas Pro, DaVinci Resolve.]
        - :blue[Photo Editing: Adobe Photoshop, Adobe Lightroom, Canva.]
        - :blue[Vector Base Editing: Adobe Illustrator.]
        - :blue[Databases: MySQL.]
        """)
        st.subheader(":blue[Work Experience]",divider='blue',anchor=False)
        st.write("""
        - :blue[Graphic Designer: Moksha Foundation(2021)]
        - :blue[Assistant: Future Vision Computers(April 2024-Present)]
        """)

        st.subheader(":blue[Educational Qualification]",divider='blue',anchor=False)
        st.write("""
        - :blue[10th: GSEB(65%)[2018]]
        - :blue[Diploma in Computer Engineering(2021-2023): 9.5CGPA]
        - :blue[Bachelors in Computer Engineering (2023-2026): 7.5CGPA]
        """)
        
        st.link_button("CONNECT WITH VANSH",url="https://vanshgurnani.streamlit.app/",type='secondary',use_container_width=True)

    def projectLink(self):
        st.divider()
        if st.button("LINK TO THE PROJECT",use_container_width=True,key='projectlink'):
            st.info("This project will be uploaded on github upon completion. Please check again later")
    



MHM=MentalHealthManagement()
MHM.keyfeatures()
MHM.Benefits()
MHM.ProjectMedia()
MHM.TeamMembers()
MHM.projectLink()