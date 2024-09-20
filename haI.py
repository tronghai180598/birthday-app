import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Title for the web page
st.title("🎉 Happy Birthday! 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Create a container for images
st.subheader("📸 Some Special Moments 📸")

# Use st.columns to display images in a row (side by side)
col1, col2, col3 = st.columns(3)

# Add images to each column
with col1:
    st.image("mua_do_uav2.png", caption="Have an amazing birthday!", use_column_width=True)

with col2:
    st.image("Kalman_filter.png", caption="Cherish every moment!", use_column_width=True)

with col3:
    st.image("kalman.png", caption="Make this day unforgettable!", use_column_width=True)

# Add a video (uncomment and replace with your video link)
# st.video("https://www.youtube.com/watch?v=YourVideoID")  

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
