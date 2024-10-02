import streamlit as st
import random

# Установить заголовок и иконку страницы
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Заголовок для веб-страницы
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Отображение поздравления с днем рождения
st.write("1 ĐỜI AN YÊN VÀ HẠNH PHÚC")

# Кнопка для сюрприза
if st.button('EM ẤN NÚT 1'):
    st.image("bánhinhnhat.PNG", caption="CHÚC MỪNG SINH NHẬT NÓC NHÀ", use_column_width=True)
    st.success("Umbala, hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh. "
               "Một ngày hết sức ý nghĩa cho em và cho cả anh nữa. "
               "Vì điều kiện không cho phép anh được ở gần em, anh muốn làm gì đó đặc biệt gửi tới em.")

if st.button('EM ẤN NÚT 2'):
    st.image("hoa hong.jfif", caption="Anh ước rằng trong thời gian gần nhất bàn tay chúng ta sẽ thay tay của họ trong ảnh này", use_column_width=True)

if st.button('EM ẤN NÚT 3'):
    video_file = open('video_nen.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

# Добавление дополнительного сообщения
st.subheader("GẦN ĐƯỢC VỀ VỚI NGA NGỐ RỒI")
st.write("HEHE. NGA NGỐ CÓ HÓNG ANH VỀ KHÔNG???")

# Инициализация состояния сессии для ответа
if 'answer' not in st.session_state:
    st.session_state.answer = None

# Вопрос для пользователя
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


# Начало игры
st.subheader("CÙNG CHƠI TRÒ CHỌN SỐ NÀO!")

# Инициализация состояния сессии для попыток и целевого числа
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
    st.session_state.target_ball = random.randint(1, 10)
    st.session_state.guessed = False

# Ввод пользователя
if st.session_state.attempts < 3:
    user_guess = st.number_input("NHẬP SỐ TỪ 1 ĐẾN 10: ", min_value=1, max_value=10)

    if st.button("ĐOÁN"):
        st.session_state.attempts += 1

        if user_guess < st.session_state.target_ball:
            st.warning("SỐ VỪA NHẬP BÉ QUÁ, THỬ LẠI ĐÊ!!")
        elif user_guess > st.session_state.target_ball:
            st.warning("SỐ VỪA NHẬP LỚN QUÁ, THỬ LẠI ĐÊ!!")
        else:
            st.success("🎉🎉CHÚC MỪNG NGA NGỐ, EM SẼ CÓ QUÀ NHÉ!🎉🎉")
            st.session_state.guessed = True

if st.session_state.attempts >= 3:
    if not st.session_state.guessed:
        st.error(f"😢 Tất cả các cơ hội đã hết! Số đúng phải là: {st.session_state.target_ball}")
    
    if st.button("CHƠI LẠI"):
        st.session_state.attempts = 0
        st.session_state.target_ball = random.randint(1, 10)
        st.session_state.guessed = False
        st.success("Chơi lại thành công! Hãy đoán lại số nào!")
