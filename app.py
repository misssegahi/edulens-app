import streamlit as st
from google import genai
from PIL import Image

# Setup your Gemini Client
client = client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


# Set up the page title and layout
st.set_page_config(page_title="EDUlens - AI Assistant", page_icon="🎓")

# Sidebar navigation for your 5 Features
st.sidebar.title("🎒 EDUlens Navigation")
feature = st.sidebar.radio(
    "Choose a Feature:",
    ["🤖 General Chat & Image Upload", "📝 Text Summarizer", "✍️ Grammar Fixer", "💻 Code Assistant", "🧠 Quiz Generator"]
)

# Feature 1: General Chat WITH Image Upload
if feature == "🤖 General Chat & Image Upload":
    st.title("🎓 EDUlens - Chat & Vision")
    
    # 📸 IMAGE UPLOAD BUTTON ADDED HERE
    uploaded_file = st.file_uploader("Upload an image for EDUlens to see (Optional):", type=["png", "jpg", "jpeg"])
    
    # Show the image if uploaded
    img = None
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Your Uploaded Image", use_container_width=True)

    user_input = st.text_input("Ask a question about your image or any educational topic:", placeholder="What is in this image?")
    
    if st.button("Ask EDUlens"):
        if user_input or img:
            with st.spinner("Analyzing..."):
                # If there's an image, send both image and text
                contents = [img, user_input] if img else user_input
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash', 
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
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                st.info(response.text)

# Feature 3: Grammar Fixer
elif feature == "✍️ Grammar Fixer":
    st.title("✍️ EDUlens - Grammar Fixer")
    user_input = st.text_area("Paste your text to check:", placeholder="i is writing code now...")
    if st.button("Fix Grammar"):
        if user_input:
            with st.spinner("Correcting..."):
                prompt = f"Correct any grammar or spelling mistakes in this text and provide the polished version:\n\n{user_input}"
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                st.success(response.text)

# Feature 4: Code Assistant
elif feature == "💻 Code Assistant":
    st.title("💻 EDUlens - Code Assistant")
    user_input = st.text_input("What code do you need help with?", placeholder="Write a Python function to sort a list.")
    if st.button("Generate Code"):
        if user_input:
            with st.spinner("Coding..."):
                prompt = f"Act as an expert software developer. Help with this programming request:\n\n{user_input}"
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                st.code(response.text)

# Feature 5: Quiz Generator
elif feature == "🧠 Quiz Generator":
    st.title("🧠 EDUlens - Quiz Generator")
    user_input = st.text_input("Enter a subject topic:", placeholder="Photosynthesis")
    if st.button("Generate Quiz"):
        if user_input:
            with st.spinner("Creating Questions..."):
                prompt = f"Create a short 3-question multiple-choice quiz about {user_input} with answers at the end."
                response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
                st.write(response.text)


