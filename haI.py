import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Title for the web page
st.title("🎉 Happy Birthday! 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Add the image (using the full path to your image)
st.image("mua_do_uav2.png", caption="Have an amazing birthday!", use_column_width=True)
# Add more images
st.image("Kalman_filter.png", caption="Cherish every moment!", use_column_width=True)
st.image("kalman.png", caption="Make this day unforgettable!", use_column_width=True)

# Add a video (use a URL from YouTube or local video file)
#st.video("https://www.youtube.com/watch?v=YourVideoID")  # Replace with the actual YouTube link
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
