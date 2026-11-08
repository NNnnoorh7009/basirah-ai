import streamlit as st
import hashlib
from urllib.parse import urlparse

st.set_page_config(page_title="Cyber Investigator App", layout="wide")

st.title("Cyber Investigator & CIA Triad Risk System")
st.divider()

tab1, tab2, tab3 = st.tabs(["URL Analysis", "File Security", "CIA Triad"])

with tab1:
    st.subheader("URL Risk & Phishing Analysis")
    url_input = st.text_input("Enter URL to scan:")
    if st.button("Start Scan"):
        if url_input:
            if "https" in url_input:
                st.success("Secure Protocol: HTTPS")
            else:
                st.warning("Insecure Protocol: HTTP")
        else:
            st.error("Please enter a URL first.")

with tab2:
    st.subheader("File Security & Hashing")
    uploaded_file = st.file_uploader("Upload a file for hashing:")
    if uploaded_file is not None:
        file_bytes = uploaded_file.read()
        sha256_val = hashlib.sha256(file_bytes).hexdigest()
        st.success(f"File Name: {uploaded_file.name}")
        st.code(sha256_val)

with tab3:
    st.subheader("CIA Triad Risk Analysis")
    st.write("Confidentiality | Integrity | Availability")
