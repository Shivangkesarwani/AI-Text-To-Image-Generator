import streamlit as st
from huggingface_hub import InferenceClient
import os

st.set_page_config(page_title="AI Text To Image Generator")

st.title("🎨 AI Text To Image Generator")

prompt = st.text_input("Enter your prompt")

if st.button("Generate Image"):

    if prompt:

        try:
            client = InferenceClient(
                api_key=os.environ["HF_TOKEN"]
            )

            image = client.text_to_image(
                prompt,
                model="black-forest-labs/FLUX.1-schnell"
            )

            st.image(
                image,
                caption="Generated Image",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a prompt.")
