import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Title for the web page
st.title("🎉 Happy Birthday! 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Initialize session state to keep track of the current image index
# if 'current_image' not in st.session_state:
#     st.session_state.current_image = 0

# List of images and their captions
# images = [
#     ("mua_do_uav2.png", "Have an amazing birthday!"),
#     ("Kalman_filter.png", "Cherish every moment!"),
#     ("kalman.png", "Make this day unforgettable!")
# ]

# Display the current image based on the session state index
# if st.session_state.current_image < len(images):
#     img_path, caption = images[st.session_state.current_image]
#     st.image(img_path, caption=caption, use_column_width=True)

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
if st.button('Click for a Special Message'):
    st.success("🎂 Enjoy your day to the fullest! 🎉")

# Add another message or text section
st.subheader("🎁 Here's a Special Wish for You! 🎁")
st.write("May all your dreams come true and may happiness always be with you!")

# Add another section for more fun or interactive content
st.subheader("🎈 A Little Party Game 🎈")
if st.button('Click to Reveal a Surprise'):
    st.balloons()  # This will make balloons fall on the screen
    st.success("🎉 You got a surprise! 🎉")
