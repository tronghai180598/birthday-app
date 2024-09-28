import streamlit as st

# Set page title and icon
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Title for the web page
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# # Display the image (Make sure to have 'fb_ngango.jpg' in the correct directory)


# Button for a surprise message
if st.button('EM ẤN NÚT 1'):
    st.success("Umbala, Hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh." " "
"Một ngày hết sức ý nghĩa cho em và cho cả anh nữa." " "
" Vì điều kiện không cho phép anh được ở gần em trong ngày tuyệt vời này nên a muốn làm gì đó đặc biệt để gửi tới em")
if st.button('EM ẤN NÚT 2'):
    st.image("fb_ngango.png", caption="Cherish every moment!", use_column_width=True)
# Add another message or text section
st.subheader("Gan duoc ve roi")
st.write("Co anh day roi.hehe")

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
