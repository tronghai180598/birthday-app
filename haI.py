import streamlit as st
import random

# Установить заголовок и иконку страницы
st.set_page_config(page_title="CHÚC MỪNG SINH NHẬT", page_icon="🎉")

# Заголовок для веб-страницы
st.title("🎉🎉 CHÚC MỪNG SINH NHẬT NGA NGỐ 🎉🎉")

# Отображение поздравления с днем рождения
st.write("1 ĐỜI AN YÊN VÀ HẠNH PHÚC")

# Поздравления и информации
if st.button('EM ẤN NÚT 1'):
    st.image("bánhinhnhat.PNG", caption="CHÚC MỪNG SINH NHẬT NÓC NHÀ", use_column_width=True)
    st.success("Umbala, hôm nay là sinh nhật cô bé Thiên Bình và hay dỗi của anh.")

if st.button('EM ẤN NÚT 2'):
    st.image("hoa hong.jfif", caption="Anh ước rằng bàn tay chúng ta sẽ thay tay của họ trong ảnh này", use_column_width=True)

if st.button('EM ẤN NÚT 3'):
    video_file = open('video_nen.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

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
