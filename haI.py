import streamlit as st

# Set page title and icon
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Title for the web page
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Display the birthday message
st.write("1 ĐỜI AN YÊN VÀ HẠNH PHÚC")

# Button for a surprise message
if st.button('EM ẤN NÚT 1'):
    st.success("Umbala, Hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh." 
               " Một ngày hết sức ý nghĩa cho em và cho cả anh nữa." 
               " Vì điều kiện không cho phép anh được ở gần em trong ngày tuyệt vời này nên anh muốn làm gì đó đặc biệt để gửi tới em")

if st.button('EM ẤN NÚT 2'):
    st.image("hoa_hong.jfif", caption="Anh ước rằng trong thời gian gần nhất bàn tay chúng ta sẽ thay tay của họ trong ảnh này", use_column_width=True)

if st.button('EM ẤN NÚT 3'):
    video_file = open('video_nen.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
    
# Add another message or text section
st.subheader("GẦN ĐƯỢC VỀ VỚI NGA NGỐ RỒI")
st.write("HEHE. NGA NGỐ CÓ HÓNG ANH VỀ KHÔNG???")
# Initialize session state for 'answer'
if 'answer' not in st.session_state:
    st.session_state.answer = None

# Ask the user for their choice
st.subheader("NGA NGỐ CÓ ĐỒNG Ý NĂM SAU VỀ DẠM NGÕ VỚI ANH KHÔNG???")

if st.session_state.answer is None:
    choice = st.radio("Chọn một đáp án:", ('YES', 'NO'))

    if st.button('GỬI'):
        if choice == 'YES':
            st.success("EM ẤN VÀO NÓ RỒI NHÉ. ANH THẤY RỒI, NĂM SAU PHẢI THỰC HIỆN ĐẤY")
            st.balloons()  # This will make balloons fall on the screen
            st.session_state.answer = "Yes"  # Save the answer
        elif choice == 'NO':
            st.warning("Chọn lại đi!")
            st.session_state.answer = "No"
else:
    # Display final message based on answer
    if st.session_state.answer == "Yes":
        st.success("Cảm ơn vì đã tham gia! Bạn đã chọn: " + st.session_state.answer)
 
