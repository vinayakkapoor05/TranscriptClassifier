import streamlit as st
import requests
import base64

def main():
    st.title("Transcript Classifier")

    uploaded_file = st.file_uploader("Upload a PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file is not None:
        if st.button("Classify Document"):
            try:
                file_bytes = uploaded_file.read()
                file_b64 = base64.b64encode(file_bytes).decode("utf-8")

                payload = {
                    "filename": uploaded_file.name,
                    "file_data": file_b64
                }

                api_url = "https://7552cs27g4.execute-api.us-east-2.amazonaws.com/prod/classify"
                response = requests.post(api_url, json=payload)

                st.write(f"**Status Code:** {response.status_code}")
                if response.ok:
                    st.json(response.json())
                else:
                    st.write("**Response Body:**", response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
