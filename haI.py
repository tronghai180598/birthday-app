import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Nga Ngo Co len", page_icon="🎉")

# Title for the web page
st.title("🎉 Yeu Nga Ngo 🎉")

# Display the birthday message
st.write("Wishing you a wonderful birthday filled with joy and happiness!")

# Display the image (Make sure to have 'fb_ngango.jpg' in the correct directory)
st.image("fb_ngango.png", caption="Cherish every moment!", use_column_width=True)

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

    # Show two buttons for "Yes" and "No" options
    col1, col2 = st.columns(2)

    with col1:
        if st.button('Yes'):
            st.success("Chuc mung em co duoc a! 🎉")

    with col2:
        if st.button('No'):
            st.error("Sai roi, can phai chon lai!")
            if st.button("Chon lai di"):
                st.experimental_rerun()  # Reloads the app to let the user choose again
