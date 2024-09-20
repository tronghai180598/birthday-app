import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Happy Birthday!", page_icon="🎉")

# Title for the web page
st.title("🎉 Happy Birthday! 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Add the image (using the full path to your image)
st.image("/home/hai/Pictures/mua_do_uav2.png", caption="Have an amazing birthday!", use_column_width=True)

# Button for a surprise message
if st.button('Click for a Special Message'):
    st.success("🎂 Enjoy your day to the fullest! 🎉")
