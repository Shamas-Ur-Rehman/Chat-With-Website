import streamlit as st 

st.set_page_config(page_title="Chat With Website" , page_icon="😊")
st.title("Chat With Website")
with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Enter Website URL")