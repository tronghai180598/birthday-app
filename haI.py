import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Nga Ngo Co len", page_icon="🎉")

# Title for the web page
st.title("🎉 Yeu Nga Ngo 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Initialize session state to keep track of the current image index
# if 'current_image' not in st.session_state:
#     st.session_state.current_image = 0

# List of images and their captions
images = [ ("fb_ngango", "Cherish every moment!")]

# Display the current image based on the session state index
if st.session_state.current_image < len(images):
    img_path, caption = images[st.session_state.current_image]
    st.image(img_path, caption=caption, use_column_width=True)

# Buttons to navigate through images
# col1, col2 = st.columns(2)

# with col1:
#     if st.button('Show Previous Image'):
#         if st.session_state.current_image > 0:
#             st.session_state.current_image -= 1
#         else:
#             st.warning("You are at the first image!")

# with col2:
#     if st.button('Show Next Image'):
#         if st.session_state.current_image < len(images) - 1:
#             st.session_state.current_image += 1
#         else:
            # st.success("🎉 You've seen all the images! 🎉")

# Button for a surprise message
if st.button('Chon nut nay di'):
    st.success("Nga Ngo Co Len")

# Add another message or text section
st.subheader("Gan duoc ve roi")
st.write("Co anh day roi.hehe")

# Add another section for more fun or interactive content
st.subheader("🎈 A Little Party Game 🎈")
if st.button('Bam vo day di'):
    st.balloons()  # This will make balloons fall on the screen
    st.success("Nga ngo yeu anh khong??? hehe")
