### Streamlit Chatbot with Security Awareness

## 🚀 Project Overview
**SafeStreamBot** is a Streamlit-based chatbot application that showcases the capabilities of advanced AI models like **DeepSeek** and **Llama**. It is designed to provide expert-level medical and general advisory responses while raising awareness about the risks of sharing sensitive API keys in third-party applications.

⚠️ **Disclaimer:** This project demonstrates how API keys can be logged into a database and text file to educate users about potential security risks. It is intended for educational purposes only.

---

## ✨ Features

### Chatbot Capabilities
- 💡 **Multi-Model Support**:
  - **DeepSeek**: Expert medical advisory.
  - **Llama Models**: General conversational AI (Llama-3.3-70b and Llama-3.1-8b).
- 🩺 **Medical Expertise**: Ask questions about health, treatments, or medical conditions.
- 📜 **Chat History Management**: Download full chat history in JSON format.
- ⚙️ **Customizable Model Selection**: Choose the model that best suits your needs.

### Key Logging Awareness
- 🛡️ Demonstrates how API keys entered by users can be logged into:
  - A secure SQLite database (`log.db`).
  - A plain text file (`log.txt`).
- 🔍 Raises awareness about potential misuse of sensitive information in third-party applications.

---

## 🛠️ How It Works

1. Users enter their API key in the Streamlit sidebar to activate the chatbot.
2. The application logs the key into both a database and a text file as part of its educational demonstration.
3. Users interact with the chatbot by selecting a model and asking questions about medical or general topics.
4. All interactions are saved in a chat history that can be downloaded as a JSON file.

---

## 📂 Repository Structure

├── app.py # Main Streamlit application code
├── test.py # Code for logging API keys (educational purpose)
├── log.db # SQLite database file (auto-created)
├── log.txt # Text file for logged API keys (auto-created)
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🔒 Security Awareness Message

This project serves as a reminder to:
1. Be cautious when entering sensitive information like API keys into third-party applications.
2. Always review the source code of an application before using it to ensure your data is handled securely.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- Streamlit installed (`pip install streamlit`)
- An active API key for Groq or other supported models.

### Installation

1. Clone this repository:
```
git clone https://github.com/Shiv-D-Coder/SafeStreamBot
cd KeyAwareBot
```

2. Install dependencies:
```   
pip install -r requirements.txt
```

3. Run the application:
```
streamlit run app.py
```


---

## 📋 Notes on `test.py`

The `test.py` script contains logic for logging API keys into both a database and a text file. While this functionality is included for educational purposes, it highlights how easily sensitive data can be stored without user knowledge.

---

## 🤝 Contributing

Contributions are welcome! If you have ideas to improve this project or want to add more features, feel free to open an issue or submit a pull request.
