from __future__ import absolute_import, division, print_function
from streamlit_webrtc import webrtc_streamer
import av
import  streamlit as st
import streamlit.components.v1 as com
import tempfile
import imutils

import streamlit as st
import streamlit.components.v1 as com
from streamlit_webrtc import webrtc_streamer

import tensorflow as tf
from imutils.video import VideoStream
import os
import numpy as np
import cv2
import av
from sklearn.svm import SVC
import glob

def uploadVideo():
    f = st.file_uploader("Upload file")
    if f is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False) 
        tfile.write(f.read())
        vf = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        while vf.isOpened():
            ret, frame = vf.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(gray)
st.subheader("Create New Account")

def check_null(infor1, infor2, infor3):
    if infor1=='' and infor2=='' and infor3=='':
        return False
    return True

foldername=""
count=0
def check_login():
    if (check_null(name, new_user, new_pass)):
        tab1, tab2= st.tabs(["Upload Video", "Open Webcam"])
        with tab1:
            st.header("Upload Video")
            uploadVideo()
        with tab2:
            st.header("Open Webcam")
            
        st.button('HOÀN THÀNH ĐĂNG KÝ')              
    else:
        st.subheader("BẠN HÃY ĐIỀN ĐỦ THÔNG TIN NHA")
           
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://img.freepik.com/free-vector/watercolor-winter-background-with-blue-flowers_52683-78685.jpg?w=1060&t=st=1669519502~exp=1669520102~hmac=4f845a71ead13bdd020b3cb267f63699ca58b0699065c11e6d05b23f2f890458');
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
name=st.text_input("Fullname")
new_user = st.text_input("Username")
new_pass = st.text_input("PassWord")
st.text("Training Face Recognition")
btn_next=st.button("Next", on_click=check_login())


    