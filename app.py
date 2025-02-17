import streamlit as st
import google.generativeai as genai
import json
import time
import config
from filter import is_solar_related

# Configure Gemini API
genai.configure(api_key=config.API_KEY)

def get_ai_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text if hasattr(response, "text") else "Error fetching response"

# Page config
st.set_page_config(
    page_title="Solar Industry AI Assistant",
    page_icon="☀️",
    layout="wide"
)

# Title
st.title("🌞 Solar Industry AI Assistant")
st.markdown("Ask any question related to solar energy, installation, cost, regulations, and more!")

# Create tabs
tab1, tab2 = st.tabs(["💬 Chat Assistant", "👤 About Me"])

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_query = st.text_area("💡 Enter your question:", height=100)
        if st.button("⚡ Get Answer"):
            if user_query.strip():
                if is_solar_related(user_query):
                    with st.spinner("Thinking...💭"):
                        response = get_ai_response(user_query)
                    st.session_state.chat_history.append({"question": user_query, "answer": response})
                    st.subheader("🤖 AI Response:")
                    st.success(response)
                else:
                    st.warning("⚠️ Please ask only solar energy-related questions.")
            else:
                st.warning("⚠️ Please enter a question.")
    
    with col2:
        st.subheader("📜 Chat History")
        if st.button("💾 Export Chat History"):
            chat_data = json.dumps(st.session_state.chat_history, indent=4)
            st.download_button("📥 Download", chat_data, "chat_history.json")
        
        for idx, chat in enumerate(st.session_state.chat_history[::-1]):
            if st.button(f"🗨️ {chat['question'][:40]}...", key=f"chat_{idx}"):
                st.markdown(f"**Q:** {chat['question']}")
                st.markdown(f"**A:** {chat['answer']}")

with tab2:
    st.header("Uditanshu Pandey")
    st.markdown("""
    **Course:** B.Tech (Artificial Intelligence & Machine Learning)  
    **College:** Delhi Technical Campus, Greater Noida  
    **Affiliation:** Guru Gobind Singh Indraprastha University, New Delhi
    """)
    
    st.subheader("👋 Introduction")
    st.write("""
    Enthusiastic and dedicated student with expertise in Python, data structures, algorithms, and machine learning. 
    Currently preparing for the GATE exam to enhance my technical knowledge. 
    Eager to contribute to unique projects and thrive in a dynamic environment.
    """)
    
    st.subheader("🛠️ Skills")
    
    st.write("**Programming Languages:**")
    st.write("Python, C++, SQL, SQLite, MongoDB, Django")
    
    st.write("**Deep Learning Frameworks:**")
    st.write("TensorFlow, Keras")
    
    st.write("**Web Framework:**")
    st.write("Django, HTML, CSS, Bootstrap, Javascript")
    
    st.write("**Libraries & Tools:**")
    st.write("NumPy, Pandas, Scikit-learn, OpenCV, NLTK, Pillow, Streamlit, Matplotlib, Seaborn, Git")
    
    # Contact section with styled buttons
    st.subheader("📬 Contact")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<a href="mailto:uditanshupandey@example.com" style="text-decoration: none;"><button style="background-color: #FF9900; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">📧 Email</button></a>', unsafe_allow_html=True)
    with col2:
        st.markdown('<a href="https://linkedin.com/in/" style="text-decoration: none;"><button style="background-color: #0077B5; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">👔 LinkedIn</button></a>', unsafe_allow_html=True)
    with col3:
        st.markdown('<a href="https://github.com/" style="text-decoration: none;"><button style="background-color: #333; color: white; border: none; padding: 10px; border-radius: 5px; width: 100%;">💻 GitHub</button></a>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("© 2025 Solar Industry AI Assistant | Developed by Uditanshu Pandey")
