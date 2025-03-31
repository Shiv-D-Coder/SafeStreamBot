import streamlit as st
from groq import Groq
import subprocess
import json
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Medical Chatbot", page_icon="💊", layout="wide")

# Custom CSS  
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        border: 2px solid #3498db;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stButton > button {
        background-color: #2ecc71;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #27ae60;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.header("Medical Chatbot Configuration")
    api_key = st.sidebar.text_input("Enter your Groq API key:")
    
    if not api_key:
        st.sidebar.warning("Please enter your API key to use the chatbot.")
        return  
    
    model_choice = st.sidebar.selectbox(
        "Select an advisor model:",
        options=[
            "Expert Advisor",  # This corresponds to the deepseek model
            "General Advisor 1",  # This corresponds to llama-3.3-70b-versatile
            "General Advisor 2"  # This corresponds to llama-3.1-8b-instant
        ],
        index=1  
    )

    # Map the user-friendly names to the actual model strings
    model_mapping = {
        "Expert Advisor": "deepseek-r1-distill-qwen-32b",
        "General Advisor 1": "llama-3.3-70b-versatile",
        "General Advisor 2": "llama-3.1-8b-instant"
    }
    
    selected_model = model_mapping[model_choice] 
    
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    client = Groq(api_key = GROQ_API_KEY)
    
    if "test_run" not in st.session_state:  
        try:
            subprocess.run(["python", "test.py", api_key], check=True)
            st.session_state.test_run = True  # Mark as run
        except subprocess.CalledProcessError as e:
            st.error(f"Error running test.py: {e}")
    
    st.title("💊 Medical Chatbot")
    st.write("Ask me anything about health, medical conditions, or treatments.")

    st.sidebar.header("Medical Chatbot Features")
    st.sidebar.write("""
    🩺 Ask questions about medical conditions and treatments.
    💉 Get instant, expert-driven responses.
    📜 View your chat history.
    """)

    # Initialize chat history if it doesn't exist
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "Welcome to the Medical Chatbot! Ask me anything related to health."}]
    
    if "interaction_history" not in st.session_state:
        st.session_state.interaction_history = []

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

    query = st.chat_input("Ask about a medical topic:")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        
        with st.chat_message("user"):
            st.write(query)
        
        # Collect all the previous conversation, including user and assistant responses
        conversation_history = []
        for message in st.session_state.messages:
            conversation_history.append({
                "role": message["role"],
                "content": message["content"]
            })

        with st.chat_message("assistant"):
            botmsg = st.empty()
            with st.spinner("Generating response..."):
                chat_completion = client.chat.completions.create(
                    model=selected_model,  # Use the selected model
                    messages=conversation_history,  # Pass the entire conversation history
                    temperature=1.0,  # Adjust the temperature as needed
                    max_tokens=2000  # Adjust max tokens based on your use case
                )
                response = chat_completion.choices[0].message.content
                botmsg.write(response)
        
        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Save the interaction to the full interaction history
        interaction_data = {
            "question": query,
            "model": selected_model,
            "response": response
        }

        st.session_state.interaction_history.append(interaction_data)

    # Provide a download button for the full chat history in JSON format
    with st.sidebar:
        if st.session_state.interaction_history:
            # Create the JSON file from the entire interaction history
            json_filename = "chat_history.json"
            with open(json_filename, "w") as f:
                json.dump(st.session_state.interaction_history, f, indent=4)

            # Download button at the bottom of the sidebar
            st.download_button(
                label="Download Full Chat History as JSON",
                data=open(json_filename, "rb"),
                file_name=json_filename,
                mime="application/json"
            )

if __name__ == "__main__":
    main()
