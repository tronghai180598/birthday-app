import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Title for the web page
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Display the birthday message
st.write("1 ĐỜI AN YÊN VÀ HẠNH PHÚC")

# Button for a surprise message
if st.button('EM ẤN NÚT 1'):
    st.image("bánhinhnhat.PNG", caption="CHÚC MỪNG SINH NHẬT NÓC NHÀ", use_column_width=True)
    st.success("Umbala, Hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh." 
               " Một ngày hết sức ý nghĩa cho em và cho cả anh nữa." 
               " Vì điều kiện không cho phép anh được ở gần em trong ngày tuyệt vời này nên anh muốn làm gì đó đặc biệt để gửi tới em")

if st.button('EM ẤN NÚT 2'):
    st.image("hoa hong.jfif", caption="Anh ước rằng trong thời gian gần nhất bàn tay chúng ta sẽ thay tay của họ trong ảnh này", use_column_width=True)

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
st.subheader("NGA NGỐ CÓ ĐỒNG Ý TẾT VỀ DẠM NGỌ VỚI ANH KHÔNG???")

if st.session_state.answer is None:
    if st.button('YES'):
        st.success("EM ẤN VÀO NÓ RỒI NHÉ. ANH THẤY RỒI, NĂM SAU PHẢI THỰC HIỆN ĐẤY")
        st.image("yeuthuong.jfif", caption="CẢM ƠN EM", use_column_width=True)
        st.balloons()
        st.session_state.answer = "Yes"

    elif st.button('NO'):
        st.session_state.answer = "No"
        st.warning("😡 Chọn lại đê! 😡")
        st.image("anh-doi-hon_102712112.jpg", caption="Anh đang rất giận đó!", use_column_width=True)

        # Изменяем текст кнопки "NO" на "YES"
        if st.button("YES", key="yes_replacement"):
            st.success("EM ẤN VÀO NÓ RỒI NHÉ. ANH THẤY RỒI, NĂM SAU PHẢI THỰC HIỆN ĐẤY")
            st.image("yeuthuong.jfif", caption="CẢM ƠN EM", use_column_width=True)
            st.balloons()
            st.session_state.answer = "Yes"

else:
    if st.session_state.answer == "Yes":
        st.success("Cảm ơn vì đã tham gia! Bạn đã chọn: " + st.session_state.answer)

    if st.button("Chọn lại"):
        st.session_state.answer = None
        st.success("Bạn có thể chọn lại!")

# Игра: Попади в шар
st.subheader("CÙNG CHƠI TRÒ CHỌN SỐ NÀO!")
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.session_state.hit = False

# Генерируем случайное число от 1 до 10 для попадания в шар
target_ball = random.randint(1, 10)

# Пользовательский ввод
user_guess = st.number_input("NHẬP SỐ TỪ 1 ĐẾN 10:", min_value=1, max_value=10)

if st.button("OK"):
    st.session_state.attempts += 1

    if user_guess == target_ball:
        st.session_state.hit = True
        st.success("🎉🎉CHÚC MỪNG NGA NGỐ, EM SẼ CÓ QUÀ NHÉ!🎉🎉")
        st.balloons()
    elif user_guess < target_ball:
        st.warning("SỐ VỪA NHẬP BÉ QUÁ, THỬ LẠI ĐÊ!!")
    else:  # В противном случае, это значит что user_guess > target_ball
        st.warning("SỐ VỪA NHẬP LỚN QUÁ, THỬ LẠI ĐÊ!!")

    if st.session_state.attempts >= 3:
        st.error("😢 Chọn sai hết rồi nhé, Số đúng phải là: " + str(target_ball))
        st.session_state.attempts = 0  # Сброс попыток для новой игры
        st.session_state.hit = False  # Сброс состояния попадания

# Отображение количества попыток
st.write(f"SỐ LƯỢT ĐÃ CHỌN: {st.session_state.attempts}/3")

# Сброс игры
if st.button("BẮT ĐẦU TRÒ CHƠI MỚI"):
    st.session_state.attempts = 0
    st.session_state.hit = False
