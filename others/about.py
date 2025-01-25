import streamlit as st
from others.forms.contactform import contact_form
from assets.custom_html import instagram_button,linkedin_button

class AboutMe:
  def __init__(self):
    st.header(':red[About Me :material/person:]',divider='red',anchor=False)
    col1,col2=st.columns(2,gap='large',vertical_alignment='top')
    with col1:
      st.html("""<p>A computer engineering student with a keen interest in both the fields of <strong>Cybersecurity</strong> and <strong>Website Development</strong>.
               My focus is to create visually appealing and user-friendly websites whilst also ensuring that strong security measures are maintained.
               The goal is to merge creativity with technical expertise that ensures a secure and attractive digital experience.<p>""")
      c1,c2=st.columns(2,gap='small',vertical_alignment='bottom')
      if c2.button("Stay in Touch",icon=":material/mail:",key='contact-button'):
        self.ContactForm()
    with col2:
      st.image("assets/Photos/MyProfile.jpg",use_container_width=True)
  @st.dialog("Contact Form")
  def ContactForm(self):
    contact_form()


  def Skills(self):


    #Experience and Qulifications
    st.subheader(":blue[Experience and Qualifications :material/work:]",divider='blue',anchor=False)
    st.write("""
    - Efficient with SQL
    - Nearly a year of experience with HTML and CSS
    - Currently working on Canteen Management System, Mental Health Management System
    - Developed a website named 'Earzz' (nearly completed).
    """)



    #Hard Skills
    st.subheader(":green[Hard Skills :material/computer:]",divider='green',anchor=False)
    st.write("""
      - Programming Skills: C, C++, HTML, CSS, JavaScript
      - Frameworks: Bootstrap
      - Databases: MySQL, MongoDB
      - Networkig Skills: OSINT, nmap-scanning, wireshark, aircrack, JohnTheRipper, netcat, pen-testing. 
    """)

    #Soft Skills
    st.subheader(":orange[Soft Skills]",divider='orange',anchor=False)
    st.write("""
    - Attention to detail
    - Adaptability
    - Leadership
    - Great team player
    - Creativity
    - Time Management
    - Problem Solving
    """)

    #Other work
    st.subheader(":grey[Other Work]",divider='grey',anchor=False)
    st.write("""
    - Currently the Sports Secretary at my college.
    - Been a part of the sponsorship committee for college events.
    - Have also been a volunteer for college events and NGOs.
    """)
  def ReachOut(self):
    st.divider()
    st.html("<H4 class='stay-in-touch'>STAY IN TOUCH</H4>")
    col1,col2=st.columns(2,gap='large',vertical_alignment='bottom')
    with col1:
      st.link_button("INSTAGRAM",url="https://www.instagram.com/maharshi__barot",type='secondary',use_container_width=True)
    with col2:
      st.link_button("LINKEDIN",url="https://www.linkedin.com/in/barot-maharshi-15b569308/",type='secondary',use_container_width=True)

AM=AboutMe()
AM.Skills()
AM.ReachOut()