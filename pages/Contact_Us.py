import streamlit as st
from PythonFiles.Sending_email import send_email

st.header("Contact Me!")

with st.form(key="contact_form"):
    email = st.text_input(label="Enter your email", key="email")
    raw_message = st.text_area(label="Enter your message", key="message")
    submit_btn = st.form_submit_button(label="Submit")
    message = f"""\
    Message from {email}\
    
    
    {raw_message}
    """

if submit_btn:
    send_email(message)
    st.info("Thanks! for contacting me. I will get back to you soon.")

