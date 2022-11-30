import streamlit as st
import streamlit.components.v1 as com
from PIL import Image

image1 = Image.open('.//Image//Chibi1.png')
image2 = Image.open('.//Image//Chibi2.png')
image3 = Image.open('.//Image//Chibi3.png')

st.title('My E-Diary')


col4, col5, col6 = st.columns([2,1.5,2.5])
with col4:
    st.subheader('''[Giới thiệu công cụ](#gioi-thieu)''')
with col5:
    st.subheader('''[Công nghệ](#cong-nghe)''')
with col6:
    st.subheader('''[Hướng dẫn sử dụng](#huong-dan)''')


    

st.subheader("Giới thiệu công cụ", "gioi-thieu")
st.text('''My E-Diary là công cụ viết nhật ký online sử dụng xác thực hai lớp để đăng nhập
         --> MẬT KHẨU 
         --> NHẬN DIỆN KHUÔN MẶT)''')

st.subheader('Công nghệ sử dụng:', "cong-nghe")
st.markdown('1. Nền tảng triển khai ứng dụng: Heroku')
st.text('Heroku là nền tảng đám mây cho phép các lập trình viên xây dựng, triển khai, quản lý và mở rộng ứng dụng (PaaS – Platform as a service).Nó rất linh hoạt và dễ sử dụng, cung cấp cho một con đường đơn giản nhất để đưa sản phẩm tiếp cận người dùng. Nó giúp các nhà phát triển tập trung vào phát triển sản phẩm mà không cần quan tâm đến việc vận hành máy chủ hay phần cứng…')
st.markdown('2. Nền tảng xây dựng ứng dụng: Streamlit')
st.text('Streamlit là một open-source Python lib, nó giúp ta dễ dàng tạo một web app cho MachineLearning và Data Science')
st.markdown('3. Cơ sở dữ liệu của ứng dụng: SQLite')
st.text('SQLite là một thư viện phần mềm mà triển khai một SQL Database Engine, không cần máy chủ, không cần cấu hình, khép kín và nhỏ gọn. Nó là một cơ sở dữ liệu, không cần cấu hình, có nghĩa là giống như các cơ sở dữ liệu khác mà bạn không cần phải cấu hình nó trong hệ thống của mình.')
st.markdown('Công nghệ nhận diện khuôn mặt: MTCNN và Facenet')
st.text('*MTCNN là viết tắt của Multi-task Cascaded Convolutional Networks. Nó là bao gồm 3 mạng CNN xếp chồng và đồng thời hoạt động khi detect khuôn mặt. Mỗi mạng có cấu trúc khác nhau và đảm nhiệm vai trò khác nhau trong task. Đầu ra của MTCNN là vị trí khuôn mặt và các điểm trên mặt như: mắt, mũi, miệng…')
st.text('*Facenet là công nghệ được Google giới thiệu năm 2015, và thằng model này thì mình cứ nhét ảnh vào (đúng size của nó) thì nó trả ra 1 vector 128 features cho 1 khuôn mặt. Sau đó dùng SVM để phân nhóm các vector đó vào các nhóm để biết vector đó là mặt của ai.')

st.subheader("Hướng dẫn sử dụng", "huong-dan")
st.markdown("Bước 1: Đăng ký tài khoản")
st.text(''' * Chọn TAB "Đăng ký"
            <Chèn ảnh ở đây>

            * Điền các thông tin cơ bản của bạn: Họ Tên, Tên Đăng nhập, Mật khẩu
            <Chèn ảnh ở đây>

            * Up video dữ liệu khuôn mặt:
            Bạn cần có video quay khuôn mặt mình quay bốn hướng (Trái, Phải , Trên , Dưới)
            !! Lưu ý: Không nên quay mặt quá nhiều (Không quá 30 độ) để đạt hiệu quả tốt nhất
            <Chèn video mẫu tại đây>

             --> Cách 1: Update video bạn đã quay sẵn
             <Chèn hình tại đây>

             --> Cách 2: Quay video trực tiếp
             <Chèn video hướng dẫn tại đây>

             * Click Đăng ký và Đợi chúng mình xử lý dữ liệu thôi ^^
             <Chèn ảnh ở đây>          
  ''')

st.markdown("Bước 2: Đăng nhập")
st.text(''' Sau khi tạo thành công tài khoản, bạn đăng nhập để sử dụng ứng dụng nhé
            * Click vào TAB "Đăng nhập"
            <Chèn ảnh ở đây>

            * Nhập tên đăng nhập và mật khẩu
            <Chèn ảnh>

            * Sau khi xác thực mật khẩu thành công, một camera sẽ mở ra để nhận diện khuôn mặt bạn
            ! Hãy cho phép ứng dụng truy cập camera nhé
            <Chèn ảnh>

            * Sau khi xác thực thành công bạn có thể bắt đầu viết nhật ký rồi ^^''')

st.markdown("Bước 3: Viết nhật ký")
st.text(''' Click TAB bạn sẽ thấy....

''')




st.subheader('Nhóm sinh viên thực hiện: Nhóm 1')

col1, col2, col3 = st.columns(3)
with col1:
    st.image(image1, use_column_width='auto')
with col2:
    st.image(image2, use_column_width='auto')
with col3:
    st.image(image3, use_column_width='auto')
    

col7, col8, col9 = st.columns(3) 
with col7:
    st.subheader("Lê Thị Kim Lệ")

with col8:
    st.subheader("Nguyễn Thị Cẩm Nguyên")

with col9:
    st.subheader("Nguyễn Thị Thùy Trang")