import streamlit as st

class SpeakForSpeechless:
    def __init__(self):
        st.header(":red[About Speak For Speechless :material/pets:]",divider='red',anchor=False)
        col1,col2=st.columns(2,gap='medium',vertical_alignment='center')
        with col1:
            st.html("""<p class='sfs-description'>
                    This foundation is committed to the rescue and rehabilitation of both wildlife and domestic animals in need. They respond to injured creatures, offering immediate treatment to alleviate their pain, whether it’s a bird, animal, reptile, or amphibian. In addition to their rescue work, they run awareness programs at schools and colleges, educating people about the importance of nature and its creatures. The foundation also supports families caring for stray animals by distributing food and water containers, and they provide bird nests during the monsoon season to ensure the safety of the birds.
                    </p>""")
        with col2:
            st.subheader(":red[Aside from my interest in technology, I am also an advocate for wildlife conservation.]",anchor=False)

    def projectMedia(self):
        st.header(":violet[My Work :material/work:]",anchor=False,divider='violet')
        with st.expander("Work Media :material/play_arrow:"):
            st.image("assets/Photos/NGO 1.jpg",caption="COBRA RESCUE")
            st.image("assets/Photos/NGO 3.jpg",caption="FUN WITH BEAGLE")
SFS=SpeakForSpeechless()
SFS.projectMedia()