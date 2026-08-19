import streamlit as st
from google import genai
from PIL import Image

# Initialize the layout and tab header first
st.set_page_config(page_title="EDUlens - AI Assistant", page_icon="🎓")

# Initialize the Gemini Client securely through Streamlit Secrets (Supports AQ. keys)
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("Configuration Error: Please verify your Streamlit Advanced Secrets dashboard setup!")

# Sidebar navigation for your 4 target features
st.sidebar.title("🎒 EDUlens Navigation")
feature = st.sidebar.radio(
    "Choose a Feature:",
    ["🤖 General Chat & Image Upload", "📝 Text Summarizer", "✍️ Grammar Fixer", "🧠 Quiz Generator"],
    key="edulens_nav_selection"
)

# ----------------- FEATURE 1: CHAT & VISION -----------------
if feature == "🤖 General Chat & Image Upload":
    st.title("🎓 EDUlens - Chat & Vision")
    uploaded_file = st.file_uploader("Upload an image for EDUlens to see (Optional):", type=["png", "jpg", "jpeg"], key="vision_uploader_tool")
    
    img = None
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Your Uploaded Image", use_container_width=True)

    user_input = st.text_input("Ask a question about your image or any educational topic:", placeholder="What is in this image?", key="vision_input_box")
    
    if st.button("Ask EDUlens", key="vision_action_btn"):
        if user_input or img:
            with st.spinner("Analyzing content..."):
                try:
                    contents = [img, user_input] if img else user_input
                    response = client.models.generate_content(
                        model='gemini-1.5-flash', 
                        contents=contents
                    )
                    st.success(response.text)
                except Exception as e:
                    st.error(f"API Request Failed: {e}\nCheck that your API key is correctly pasted in Secrets.")
        else:
            st.warning("Please type a question or upload an image first!")

# ----------------- FEATURE 2: TEXT SUMMARIZER -----------------
elif feature == "📝 Text Summarizer":
    st.title("📝 EDUlens - Text Summarizer")
    user_input = st.text_area("Paste your long text here:", placeholder="Paste text to condense...", key="summarizer_input_area")
    if st.button("Summarize Text", key="summarizer_action_btn"):
        if user_input:
            with st.spinner("Condensing..."):
                try:
                    prompt = f"Summarize the following text clearly and concisely:\n\n{user_input}"
                    response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                    st.info(response.text)
                except Exception as e:
                    st.error(f"Execution Error: {e}")
        else:
            st.warning("Please enter text to summarize.")

# ----------------- FEATURE 3: GRAMMAR FIXER -----------------
elif feature == "✍️ Grammar Fixer":
    st.title("✍️ EDUlens - Grammar Fixer")
    user_input = st.text_area("Paste your text to check:", placeholder="i is writing code now...", key="grammar_input_area")
    if st.button("Fix Grammar & Spelling", key="grammar_action_btn"):
        if user_input:
            with st.spinner("Polishing writing..."):
                try:
                    prompt = f"Correct any grammar or spelling mistakes in this text and provide the polished version:\n\n{user_input}"
                    response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Execution Error: {e}")
        else:
            st.warning("Please enter text to fix.")

# ----------------- FEATURE 4: QUIZ GENERATOR -----------------
elif feature == "🧠 Quiz Generator":
    st.title("🧠 EDUlens - Quiz Generator")
    user_input = st.text_input("Enter a subject topic:", placeholder="Photosynthesis", key="quiz_topic_input")
    if st.button("Generate Custom Quiz", key="quiz_action_btn"):
        if user_input:
            with st.spinner("Formulating quiz questions..."):
                try:
                    prompt = f"Create a short 3-question multiple-choice quiz about {user_input} with answers at the end."
                    response = client.models.generate_content(model='gemini-1.5-flash', contents=prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Execution Error: {e}")
        else:
            st.warning("Please enter a subject topic first.")
