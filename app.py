import streamlit as st
import google.generativeai as genai
from PIL import Image

# Initialize the Gemini configuration securely using Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Secrets Configuration Error: Make sure GEMINI_API_KEY is saved in your Streamlit dashboard settings!")

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
                try:
                    model = genai.InteractiveModel(model_name='models/gemini-1.5-flash') if img else genai.GenerativeModel('models/gemini-1.5-flash')
                    contents = [img, user_input] if img else user_input
                    
                    if img:
                        # For multimodal inputs
                        model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = model.generate_content([img, user_input] if user_input else [img])
                    else:
                        model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = model.generate_content(user_input)
                        
                    st.success(response.text)
                except Exception as e:
                    st.error(f"API Connection Error: {e}\nPlease check if your API Key in Streamlit Secrets is valid.")
        else:
            st.warning("Please type a question or upload an image first!")

# Feature 2: Text Summarizer
elif feature == "📝 Text Summarizer":
    st.title("📝 EDUlens - Text Summarizer")
    user_input = st.text_area("Paste your long text here:", placeholder="Paste text to condense...")
    if st.button("Summarize"):
        if user_input:
            with st.spinner("Summarizing..."):
                try:
                    prompt = f"Summarize the following text clearly and concisely:\n\n{user_input}"
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter text to summarize.")

# Feature 3: Grammar Fixer
elif feature == "✍️ Grammar Fixer":
    st.title("✍️ EDUlens - Grammar Fixer")
    user_input = st.text_area("Paste your text to check:", placeholder="i is writing code now...")
    if st.button("Fix Grammar"):
        if user_input:
            with st.spinner("Correcting..."):
                try:
                    prompt = f"Correct any grammar or spelling mistakes in this text and provide the polished version:\n\n{user_input}"
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter text to fix.")

# Feature 4: Quiz Generator
elif feature == "🧠 Quiz Generator":
    st.title("🧠 EDUlens - Quiz Generator")
    user_input = st.text_input("Enter a subject topic:", placeholder="Photosynthesis")
    if st.button("Generate Quiz"):
        if user_input:
            with st.spinner("Creating Questions..."):
                try:
                    prompt = f"Create a short 3-question multiple-choice quiz about {user_input} with answers at the end."
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a subject topic first.")
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Initialize the Gemini configuration securely using Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Secrets Configuration Error: Make sure GEMINI_API_KEY is saved in your Streamlit dashboard settings!")

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
                try:
                    model = genai.InteractiveModel(model_name='models/gemini-1.5-flash') if img else genai.GenerativeModel('models/gemini-1.5-flash')
                    contents = [img, user_input] if img else user_input
                    
                    if img:
                        # For multimodal inputs
                        model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = model.generate_content([img, user_input] if user_input else [img])
                    else:
                        model = genai.GenerativeModel('models/gemini-1.5-flash')
                        response = model.generate_content(user_input)
                        
                    st.success(response.text)
                except Exception as e:
                    st.error(f"API Connection Error: {e}\nPlease check if your API Key in Streamlit Secrets is valid.")
        else:
            st.warning("Please type a question or upload an image first!")

# Feature 2: Text Summarizer
elif feature == "📝 Text Summarizer":
    st.title("📝 EDUlens - Text Summarizer")
    user_input = st.text_area("Paste your long text here:", placeholder="Paste text to condense...")
    if st.button("Summarize"):
        if user_input:
            with st.spinner("Summarizing..."):
                try:
                    prompt = f"Summarize the following text clearly and concisely:\n\n{user_input}"
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter text to summarize.")

# Feature 3: Grammar Fixer
elif feature == "✍️ Grammar Fixer":
    st.title("✍️ EDUlens - Grammar Fixer")
    user_input = st.text_area("Paste your text to check:", placeholder="i is writing code now...")
    if st.button("Fix Grammar"):
        if user_input:
            with st.spinner("Correcting..."):
                try:
                    prompt = f"Correct any grammar or spelling mistakes in this text and provide the polished version:\n\n{user_input}"
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter text to fix.")

# Feature 4: Quiz Generator
elif feature == "🧠 Quiz Generator":
    st.title("🧠 EDUlens - Quiz Generator")
    user_input = st.text_input("Enter a subject topic:", placeholder="Photosynthesis")
    if st.button("Generate Quiz"):
        if user_input:
            with st.spinner("Creating Questions..."):
                try:
                    prompt = f"Create a short 3-question multiple-choice quiz about {user_input} with answers at the end."
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a subject topic first.")
