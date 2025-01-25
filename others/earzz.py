import streamlit as st


class Earzz:
  def __init__(self):
    st.header(":red[About Earzz :material/headphones:]",divider='red',anchor=False)
    col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
    with col1:
      st.html("""<p class='earzz-description'>
      This project focuses on designing and deploying an innovative home security system using advanced sound recognition AI to provide customizable alerts for specific sounds, offering users greater peace of mind and convenience. The system integrates seamlessly with mobile devices and offers easy setup, making it ideal for homeowners who seek a smart, responsive, and intuitive security solution.
      </p>""")
    with col2:
      st.subheader(":red[This project is still under development :material/construction:]",anchor=False)

  def features_and_questions(self):
    st.header(":green[Features :material/featured_play_list:]",anchor=False,divider='green')
    st.write("""
    - Alerts for specific sounds
    - Vibration, auditory and visual alerts for specific sounds
    - Alerts delivered anywhere with a data connection iOS & Android phone, watch & tablet
    - Cutting-edge Sound recognition Al
    - Multi-sound alerting using a single monitor
    - Cutting-edge Sound recognition Al
    """)

    st.header(":blue[Plans :material/subscriptions:]",anchor=False,divider='blue')
    st.subheader(":blue[7.99:material/currency_pound:/month]",anchor=False)
    st.write("""
      - Alerts single and multiple sounds simultaneously
      - Alerts delivered to iOS & Android devices with no location restriction as standard -  No additional cost
      - Innovative AI technology that learns and improves based on your feedback
      - Customizable Alerts
      - 2 Cameras Included
    """)

    st.divider()

    st.header(":grey[Common Questions]",anchor=False)
    st.subheader(":orange[Is Earzz easy to install??]",anchor=False,divider='orange')
    st.write("""
      Yes, Earzz is designed for easy installation and can be set up in minutes using our step-by-step guide. Please go to earzz.com/how-to
    """)
    
    st.subheader(":orange[How do I customise my notification settings for my Earzz device?]",anchor=False,divider='orange')
    st.write("""
    Tap the "Edit device Settings" button to take you into device settings, and select the "edit notification preferences" option to configure the devices you wish to be notified on. You may also pause all notifications or delete devices you no longer wish to be notified on  
    """)

    st.subheader(":orange[How many sounds can my Earzz device listen for?]",anchor=False,divider='orange')
    st.write("""
    Currently, you can listen for up to six sounds at the same time.
    """)


  def Content(self):
    st.divider()
    st.header(":violet[The Project :material/tactic:]",anchor=False,divider='violet')

    with st.expander("Project :material/play_arrow:"):
      st.image(caption='Earzz Home Page',image="assets/Photos/Earzz_page.jpeg")
      st.video(data="assets/Videos/Earzz_video.mp4",format='video/mp4',autoplay=True,muted=True,loop=True)

E=Earzz()
E.features_and_questions()
E.Content()