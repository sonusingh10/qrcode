import io
import qrcode
import streamlit as st


st.title("QRCode Generator")
st.caption("Like & follow for more! This is Sonu Singh Youtube channel")


url = st.text_input(
    "URL to encode:", 
    "https://www.youtube.com/@explo20"
)


img = qrcode.make(url)
virtualfile = io.BytesIO()
img.save(virtualfile)


st.image(virtualfile)
