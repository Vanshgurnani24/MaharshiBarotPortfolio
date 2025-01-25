import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import re


conn=st.connection(name='gsheets',type=GSheetsConnection)
existing_data=conn.read(worksheet='Contacts',usecols=list(range(6)),ttl=5)

existing_data=existing_data.dropna(how='all')

def validate_email(email):    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def contact_form():
    with st.form('Contact_Form'):
        name=st.text_input("Name",placeholder="Your name")
        Number=st.text_input("Number",placeholder="Your Mobile number")
        Email=st.text_input("Email",placeholder="Your email address")
        Company=st.text_input("Company",placeholder="Your company(optional)")
        Message=st.text_area("Message", placeholder="Your message")
        if st.form_submit_button('submit'):
            if not name:
                st.error("Name is required")
                return
            if not Number or len(Number)!=10 or not(Number.isdigit()):
                st.error("Please enter a valid 10-digit number")
                return
            if not Email or not validate_email(Email):
                st.error("Please enter a valid email address")
                return
            if not Message:
                st.error("Message is required")
                return
            
            user_data=pd.DataFrame(
                [
                    {
                        "Name": name,
                        "Number": Number,
                        "Email": Email,
                        "Company": Company,
                        "Message": Message,
                        "Date": pd.Timestamp.now()
                    }
                ]
            )
            updated_df=pd.concat([existing_data,user_data],ignore_index=True)
            conn.update(worksheet="Contacts",data=updated_df)
            st.success("Message sent successfully!")
