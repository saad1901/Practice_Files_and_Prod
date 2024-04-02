import os
import requests
from bs4 import BeautifulSoup
import streamlit as st
selection = "App Store"
if selection == 'App Store':
    uploads_dir = "uploads"
    os.makedirs(uploads_dir, exist_ok=True)
    
    def get_available_files():
        files = []
        for filename in os.listdir(uploads_dir):
            files.append(filename)
        return files

    def upload_file():
        uploaded_file = st.file_uploader("Choose a file to upload")
        if uploaded_file is not None:
            filepath = os.path.join(uploads_dir, uploaded_file.name)
            with open(filepath, "wb") as f:
                f.write(uploaded_file.read())
            st.success("File uploaded successfully!")

    def download_file(filename):
        filepath = os.path.join(uploads_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                content = f.read()
            return content
        else:
            st.error(f"File '{filename}' not found")

    def get_package_logo(package_name):
        # Fetch package logo from PyPI
        response = requests.get(f"https://pypi.org/project/{package_name}/")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            logo_tag = soup.find("img", class_="package-snippet__image")
            if logo_tag:
                return logo_tag["src"]
        return None

    st.subheader("Packages")
    st.text("Upload Files")
    st.info('under development :/')
    upload_file()

    st.subheader("Download Files")
    available_files = get_available_files()
    if available_files:
        for filename in available_files:
            file_data = download_file(filename)
            if file_data is not None:
                package_name = filename.split(".")[0]  # Extracting package name from filename
                package_logo_url = get_package_logo(package_name)
                if package_logo_url:
                    st.image(package_logo_url, caption=package_name, use_column_width=True)
                else:
                    st.write(package_name)  # Display package name if logo is not available
                st.download_button(label=filename, data=file_data, file_name=filename)
    else:
        # st.info("No files uploaded yet!")
        pass
