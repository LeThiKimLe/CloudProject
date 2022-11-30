
import streamlit as st
import streamlit.components.v1 as com

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url('https://i.pinimg.com/originals/62/e7/c9/62e7c9c10747ae9de6b30ec5a470ce4c.jpg');
background-size: 30%;
background-position: center;
background-repeat: initial;
background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
# thiết lập menu
with st.sidebar:
    col1, col2 = st.columns(2)

    with col1:
        ngay = st.date_input('Chọn ngày')

    with col2:
        gio = st.time_input("Giờ")
    new_pages = st.button("New Pages")    

com.html(
    """
    <h1 style  = "color:white"> NHẬT KÍ CỦA TÔI</h1> <br>
    <br>
    """, height=60
)

col1, col2, col3 = st.columns(3)
with col3: 
    st.write(ngay)

com.html(
    """
    <form>
        <h2 style  = "color:white" >Tiêu đề nhật kí </h2>
        <textarea rows="2" cols="80" name="comment" form="usrform"> 
        </textarea><br><br>
        <h2 style  = "color:white" >Nội dung nhật kí</h2>
        <textarea rows="15" cols="80" name="comment" form="usrform"> 
        </textarea><br><br><br>
        <input type="submit" value="Save">
    </form> 
    """, height=600
)



