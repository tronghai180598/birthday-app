import streamlit as st

# Set page title and icon
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Title for the web page
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Display the birthday message
st.write("1 ĐỜI AN YÊN VÀ HẠNH PHÚC")

# Button for a surprise message
if st.button('EM ẤN NÚT 1'):
    st.success("Umbala, Hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh." " "
               "Một ngày hết sức ý nghĩa cho em và cho cả anh nữa." " "
               "Vì điều kiện không cho phép anh được ở gần em trong ngày tuyệt vời này nên a muốn làm gì đó đặc biệt để gửi tới em")
if st.button('EM ẤN NÚT 2'):
    st.image("hoa hong.jfif", caption="Anh ước rằng trong thời gian gần nhất bàn tay chúng chúng ta sẽ thay tay của họ trong ảnh này", use_column_width=True)
if st.button('EM ẤN NÚT 3'):
    # Password-protected section
    st.subheader("🔒 Password Protected Video Section")
    password = st.text_input("Nhập Mật Khẩu Đi Bạn Êi:", type="password")

    if password == "Ngango":  # Replace with your desired password
        st.success("Access granted!")
        video_file = open('path_to_your_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes))
    else:
        st.error("Access denied. Incorrect password.")

# Add another message or text section
st.subheader("GẦN ĐƯỢC VỀ VỚI NGA NGỐ RỒI")
st.write("HEHE. NGA NGỐ CÓ HÓNG ANH VỀ KHÔNG???")


# Add another section for more fun or interactive content
st.subheader("🎈 A Little Party Game 🎈")
if st.button('Bam vo day di'):
    st.balloons()  # This will make balloons fall on the screen
    st.success("Nga ngo yeu anh khong??? hehe")

    # Initialize session state for 'answer' to track user's choice
    if 'answer' not in st.session_state:
        st.session_state.answer = None

    # Radio button for choice between Yes and No
    choice = st.radio("Select an answer:", ("Yes", "No"))

    if choice == "Yes":
        st.success("Chuc mung em co duoc a! 🎉")
        st.session_state.answer = "Yes"  # Stop asking when Yes is selected
    elif choice == "No":
        st.warning("Sai roi, can phai chon lai!")
        st.session_state.answer = "No"

    # If 'No' was selected, show the question again
    if st.session_state.answer == "No":
        st.warning("Chon lai di!")
