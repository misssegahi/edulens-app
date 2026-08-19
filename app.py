import streamlit as st
from google import genai
from PIL import Image

# Initialize the Gemini Client securely through Streamlit Secrets
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Configure layout and browser tab details
st.set_page_config(page_title="EDUlens - AI Assistant", page_icon="🎓")

# Sidebar navigation containing exactly your 4 functional features
st.sidebar.title("🎒 EDUlens Navigation")
feature = st.sidebar.radio(
    "Choose a Feature:",
    ["🤖 General Chat & Image Upload", "📝 Text Summarizer", "✍️ Grammar Fixer", "🧠 Quiz Generator"]
)

# Feature 1: General Chat WITH Image Upload (Multimodal Support)
if feature == "🤖 General Chat & Image Upload":
    st.title("🎓 EDUlens - Chat & Vision")
    uploaded_file = st.file_uploader("Upload an image for EDUlens to see (Optional):", type=["png", "jpg", "jpeg"])
    
    img = None
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Your Uploaded Image", use_container_width=True)

    user_input = st.text_input("Ask a question about your image or any educational topic:", placeholder="What is in this image?")
    
    if st.button("Ask EDUlens"):
        if user_input or img:
            with st.spinner("Analyzing..."):
                # Pass both image object and text string seamlessly if an image exists
                contents = [img, user_input] if img else user_input
                response = client.models.generate_content(
                    model='gemini-1.5-flash', 
                    contents=contents
                )
                st.success(response.text)
        else:
            st.warning("Please type a question or upload an image first!")

# Feature 2: Text Summarizer
elif feature == "📝 Text Summarizer":
    st.title("📝 EDUlens - Text Summarizer")
    user_input = st.text_area("Paste your long text here:", placeholder="Paste text to condense...")
    if st.button("Summarize"):
        if user_input:
            with st.spinner("Summarizing..."):
                prompt = f"Summarize the following text clearly and concisely:\n\n{user_input}"
                response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                st.info(response.text)
        else:
            st.warning("Please enter text to summarize.")

# Feature 3: Grammar Fixer
elif feature == "✍️ Grammar Fixer":
    st.title("✍️ EDUlens - Grammar Fixer")
    user_input = st.text_area("Paste your text to check:", placeholder="i is writing code now...")
    if st.button("Fix Grammar"):
        if user_input:
            with st.spinner("Correcting..."):
                prompt = f"Correct any grammar or spelling mistakes in this text and provide the polished version:\n\n{user_input}"
                response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                st.success(response.text)
        else:
            st.warning("Please enter text to fix.")

# Feature 4: Quiz Generator
elif feature == "🧠 Quiz Generator":
    st.title("🧠 EDUlens - Quiz Generator")
    user_input = st.text_input("Enter a subject topic:", placeholder="Photosynthesis")
    if st.button("Generate Quiz"):
        if user_input:
            with st.spinner("Creating Questions..."):
                prompt = f"Create a short 3-question multiple-choice quiz about {user_input} with answers at the end."
                response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                st.write(response.text)
        else:
            st.warning("Please enter a subject topic first.")



