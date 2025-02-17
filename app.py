import streamlit as st
import google.generativeai as genai
import os
import config
import json
import time
from filter import is_solar_related  # Import the solar query filter

# Configure Gemini API
genai.configure(api_key=config.API_KEY)

def get_ai_response(user_input):
    model = genai.GenerativeModel("gemini-pro")  # Using Gemini Pro model
    response = model.generate_content(user_input)
    return response.text if hasattr(response, "text") else "Error fetching response"

# Set page config
st.set_page_config(
    page_title="Solar Industry AI Assistant",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced UI
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem !important;
        color: #FF9900 !important;
        text-align: center;
        margin-bottom: 1rem;
        text-shadow: 1px 1px 2px #00000030;
    }
    .stButton>button {
        background-color: #FF9900;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        border: none;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #E68A00;
        transform: translateY(-2px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .query-box {
        border: 2px solid #FF9900;
        border-radius: 10px;
        padding: 10px;
    }
    .chat-container {
        border-radius: 10px;
        padding: 15px;
        margin-top: 20px;
        background-color: #f8f9fa;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .sidebar-content {
        padding: 15px;
    }
    .profile-container {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .profile-image {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        margin: 0 auto;
        display: block;
        border: 3px solid #FF9900;
    }
    .divider {
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-top: 1px solid #e9ecef;
    }
    .skill-tag {
        background-color: #FF9900;
        color: white;
        padding: 0.2rem 0.5rem;
        border-radius: 5px;
        margin-right: 5px;
        margin-bottom: 5px;
        display: inline-block;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Title with custom styling
st.markdown('<h1 class="main-title">🌞 Solar Industry AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem;">🔍 <b>Ask any question related to solar energy, installation, cost, regulations, and more!</b></p>', unsafe_allow_html=True)

# Session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Create tabs for main content and about section
tab1, tab2 = st.tabs(["💬 Chat Assistant", "👤 About Me"])

with tab1:
    # Layout with columns in the main chat tab
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Query input with enhanced styling
        st.markdown('<div class="query-box">', unsafe_allow_html=True)
        user_query = st.text_area("💡 Enter your question:", height=100)
        submit_button = st.button("⚡ Get Answer", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        if submit_button:
            if user_query.strip():
                if is_solar_related(user_query):  # Check if the query is solar-related
                    with st.spinner("Thinking...💭"):
                        time.sleep(1)  # Simulate thinking animation
                        response = get_ai_response(user_query)
                    st.session_state.chat_history.append({"question": user_query, "answer": response})
                    
                    # Display the current response in a nice box
                    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
                    st.subheader("🤖 AI Response:")
                    st.success(response)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("⚠️ Please ask only solar energy-related questions.")
            else:
                st.warning("⚠️ Please enter a question.")
    
    # Chat history in sidebar in the main chat tab
    with col2:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.subheader("📜 Chat History")
        
        # Export Chat History button
        if st.button("💾 Export Chat History", key="export_btn"):
            chat_data = json.dumps(st.session_state.chat_history, indent=4)
            st.download_button("📥 Download", chat_data, "chat_history.json", "application/json")
        
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        
        # Display chat history items
        for idx, chat in enumerate(st.session_state.chat_history[::-1]):
            if st.button(f"🗨️ {chat['question'][:40]}...", key=f"chat_{idx}"):
                st.markdown(f"**Q:** {chat['question']}")
                st.markdown(f"**A:** {chat['answer']}")
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# About Me Tab
with tab2:
    st.markdown('<div class="profile-container">', unsafe_allow_html=True)
    
    # Profile section with columns for photo and details
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Profile image placeholder (replace URL with actual image if available)
        st.markdown('<img src="https://github.com/UditanshuPandey/uditanshupandey.github.io/blob/main/imgs/Photo.png" class="profile-image">', unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h2 style='color: #FF9900;'>Uditanshu Pandey</h2>", unsafe_allow_html=True)
        st.markdown("<p><b>Course:</b> B.Tech (Artificial Intelligence & Machine Learning)</p>", unsafe_allow_html=True)
        st.markdown("<p><b>College:</b> Delhi Technical Campus, Greater Noida</p>", unsafe_allow_html=True)
        st.markdown("<p><b>Affiliation:</b> Guru Gobind Singh Indraprastha University, New Delhi</p>", unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Introduction
    st.subheader("👋 Introduction")
    st.write("""
    Enthusiastic and dedicated student with expertise in Python, data structures, algorithms, and machine learning. 
    Proficient with scikit-learn, tensorflow, numpy, and pandas. Experienced with natural language processing. 
    Currently preparing for the GATE exam to enhance my technical knowledge. 
    I am eager to contribute to unique projects and thrive in a dynamic environment.
    """)
    
    # Skills section
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.subheader("🛠️ Skills")
    
    # Programming Languages
    st.write("**Programming Languages:**")
    st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 5px;">' + 
                '<span class="skill-tag">Python</span>' +
                '<span class="skill-tag">C++</span>' +
                '<span class="skill-tag">Java</span>' +
                '</div>', unsafe_allow_html=True)
    
    # Frameworks & Libraries
    st.write("**Frameworks & Libraries:**")
    st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 5px;">' + 
                '<span class="skill-tag">TensorFlow</span>' +
                '<span class="skill-tag">Scikit-learn</span>' +
                '<span class="skill-tag">NumPy</span>' +
                '<span class="skill-tag">Pandas</span>' +
                '<span class="skill-tag">Streamlit</span>' +
                '</div>', unsafe_allow_html=True)
    
    # Areas of Interest
    st.write("**Areas of Interest:**")
    st.markdown('<div style="display: flex; flex-wrap: wrap; gap: 5px;">' + 
                '<span class="skill-tag">Machine Learning</span>' +
                '<span class="skill-tag">Natural Language Processing</span>' +
                '<span class="skill-tag">Data Structures</span>' +
                '<span class="skill-tag">Algorithms</span>' +
                '<span class="skill-tag">Solar Energy</span>' +
                '</div>', unsafe_allow_html=True)
    
    # Contact information
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.subheader("📬 Contact")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<a href="mailto:uditanshup114@gmail.com" style="text-decoration: none;"><button style="background-color: #FF9900; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">📧 Email</button></a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="linkedin.com/in/uditanshupandey" style="text-decoration: none;"><button style="background-color: #0077B5; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">👔 LinkedIn</button></a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<a href="https://github.com/UditanshuPandey" style="text-decoration: none;"><button style="background-color: #333; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">💻 GitHub</button></a>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666;">© 2025 Solar Industry AI Assistant | Developed by Uditanshu Pandey</p>', unsafe_allow_html=True)
