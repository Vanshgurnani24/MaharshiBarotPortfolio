import streamlit as st

class CanteenManagementSystem:
    def __init__(self):
        st.header(":red[About CMS :material/restaurant:]",anchor=False,divider='red')
        col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
        with col1:
            st.html("""<p class='cms-descritpion'>This project aims to develop a Canteen Management System that enhances operational efficiency, improves customer satisfaction, and provides valuable insights for better management. By automating key processes such as order management, inventory tracking, and billing, the system streamlines operations and reduces wait times for customers. Additionally, it incorporates features for user feedback, enabling continuous improvement in service quality.</p>""")
        with col2:
            st.subheader(":red[This project is still under development :material/construction:]",anchor=False)

    def keyfeatures(self):
        st.divider()
        st.header(":grey[Key Features :material/key:]",anchor=False,divider='grey')
        st.write("""
        - :grey[Menu Management]
        - :grey[Order Management]
        - :grey[Inventory Management]
        - :grey[Billing and Payment Processing]
        - :grey[User Management]
        - :grey[Reporting and Analytics]
        - :grey[Feedback and Rating System]
        - :grey[Security Features]
        - :grey[Easy Access Across devices with web and internet support]        
        """)
    def benefits(self):
        st.header(":green[Benefits :material/loyalty:]",anchor=False,divider='green')
        st.write("""
        - :green[Efficiency]
        - :green[Accuracy]
        - :green[Customer Satisfaction]
        - :green[Cost Management]
        - :green[Data-Driven Decisions]
        """)

    def projectMedia(self):
        with st.expander("Project :material/play_arrow:"):
            st.html("<H5 style='text-align: center;'>PROJECT PROTOTYPE VIDEO</H5>")
            st.video(data="assets/Videos/CMS video.mp4",format="video/mp4",autoplay=True,loop=True,muted=True)
            st.write("""
                - :violet[Note: This project is still under development and has not yet been deployed to GitHub. Once completed, it will be available for download and use on GitHub.]
            """)  
    
    def projectlink(self):
        st.divider()
        if st.button("LINK TO THE PROJECT",use_container_width=True,key='projectlink'):
            st.info("This project will be uploaded on github upon completion. Please check again later")

        

CMS=CanteenManagementSystem()
CMS.keyfeatures()
CMS.benefits()
CMS.projectMedia()
CMS.projectlink()