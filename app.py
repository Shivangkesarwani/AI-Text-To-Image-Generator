import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Text To Image Generator")

st.title("🎨 AI Text To Image Generator")

prompt = st.text_input("Enter your prompt")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"

API_TOKEN = "apply your token hear"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

if st.button("Generate Image"):

    if prompt:

        with st.spinner("Generating Image..."):

            try:
                st.write("Sending request...")

                response = requests.post(
                    API_URL,
                    headers=headers,
                    json={"inputs": prompt},
                    timeout=60
                )

                st.write(f"Status Code: {response.status_code}")

                if response.status_code == 200:

                    image = Image.open(BytesIO(response.content))

                    st.image(
                        image,
                        caption="Generated Image",
                        use_container_width=True
                    )

                else:
                    st.error("Image generation failed.")
                    st.write(response.text)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")