import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

# Configure the AI model (Replace with your actual API key or use environment variables)
# get a free key from Google AI Studio
API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Initialize the Gemini Vision model for handling both text and images
model = genai.GenerativeModel('gemini-1.5-flash')

# Set up page configurations
st.set_page_config(page_title="Edulens AI - Homework Assistant", page_icon="📚", layout="centered")

st.title("📚 Edulens AI")
st.subheader("Your ultimate AI-powered study companion")
st.write("Upload a photo of your homework or type a problem to get step-by-step explanations.")

# Input options: Text problem
text_input = st.text_area("Type your homework question here:", placeholder="e.g., Solve for x: 2x + 5 = 15, or paste an essay prompt...")

# Input options: Image upload (OCR & Visual Problem Solving)
uploaded_file = st.file_uploader("Or upload a photo of your assignment:", type=["jpg", "jpeg", "png"])

# Preview uploaded image
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Homework Image", use_column_width=True)

# System prompt to enforce educational step-by-step guidance
system_prompt = """
You are an expert AI tutor. Your goal is to help students learn by breaking down 
complex academic questions (math, science, grammar, etc.) into clear, step-by-step explanations.
Do not just provide a flat answer; explain the 'why' and 'how' behind the concept so the student can understand it.
"""

# Submit button logic
if st.button("Solve & Explain"):
    if not text_input and image is None:
        st.warning("Please provide a question by either typing text or uploading an image.")
    else:
        with st.spinner("Analyzing your homework..."):
            try:
                # Combine inputs based on what the user provided
                content_payload = [system_prompt]
                
                if text_input:
                    content_payload.append(f"Question: {text_input}")
                if image:
                    content_payload.append(image)
                    content_payload.append("Please perform OCR to read this image and solve the problem inside it.")

                # Generate the solution
                response = model.generate_content(content_payload)
                
                # Display output
                st.success("Analysis Complete!")
                st.markdown("### 📝 Step-by-Step Solution:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred while generating the solution: {e}")

st.info("Tip: Double-check the steps to master the core topic before your next exam!")
