import streamlit as st
from utils import analyze_rooftop, format_results

st.set_page_config(page_title="Solar Industry AI Assistant", layout="centered")

st.title("☀️ Solar Industry AI Assistant")
st.markdown("Upload a rooftop satellite image to assess solar panel installation potential.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Rooftop", use_column_width=True)
    with st.spinner("Analyzing rooftop..."):
        results = analyze_rooftop(uploaded_file)
        st.success("Analysis Complete")
        st.markdown(format_results(results))
