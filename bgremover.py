import streamlit as st
from rembg import remove
from PIL import Image
import io
import time


st.markdown(
    "<h1 style='text-align: center; color: #ecd07c; font-size: 42px; white-space: nowrap;'>✨ ClearCut - Background Remover ✨</h1>", 
    unsafe_allow_html=True
)

st.markdown("<p style='text-align: center; color: #999999;'>Bring Focus to Your Photos by Making Backgrounds Disappear!</p>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
  
    image = Image.open(uploaded_file)
  
    col1, col2 = st.columns(2)
    col1.image(image, caption="Original Image", use_column_width=True)
    
    with st.spinner("Removing background... this might take a moment ✨"):
        
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.02)  
            progress.progress(i + 1)
        
        output = remove(image)
        col2.image(output, caption="Without Background", use_column_width=True)
    
    st.success("Background removed successfully! 🎉")
    st.balloons()

   
    output_io = io.BytesIO()
    output.save(output_io, format="PNG")
    output_io.seek(0)

    
    col2.download_button(
        label="Download Image without Background",
        data=output_io,
        file_name="ClearCut.png",
        mime="image/png"
    )
else:
    st.info("Please upload an image to start removing the background.")

