from streamlit_webrtc import webrtc_streamer
import  streamlit as st
import streamlit.components.v1 as com
st.subheader("Sign up")
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://img.freepik.com/free-photo/tulip-flowers-with-small-hearts_23-2148094219.jpg?w=1060&t=st=1669533361~exp=1669533961~hmac=902e176480de0f4ebbb5115e6c5a0ced8ffc6bc0d43726c5392b871a5af52544');
background-size: 100%;
background-position: center;
background-repeat: initial;
background-attachment: fixed;
background-repeat: no-repeat;
}

[data-testid="stHeader"]{
    backgrounf-color: rgba(0,0,0,0);   
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
username = st.text_input("Username")
password = st.text_input("PassWord",type='password')
if (username=="admin" and password=="123"):
    with st.expander("Turn on Webcam"):
        webrtc_streamer(key="example")    
elif username!="" and password !="":
    st.write("Username or Password is incorrect")