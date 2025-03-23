# 🎥 Multimodal Agentic AI Video Summarizer

An AI-powered Streamlit app that uses **Agentic AI** to analyze and summarize video content based on your custom queries. Built with **Phidata Agents**, **Google Gemini 2.0 Flash**, and **DuckDuckGo tool** for real-time web insights.

## 🚀 Features

- 📤 Upload a video (MP4, MOV, AVI)
- 🤖 AI Agent analyzes video using Gemini 2.0 Flash
- 🌐 Augments response with real-time web search (DuckDuckGo Tool)
- 🧠 Responds to your specific query about the video
- 🖥️ Clean, interactive UI built with Streamlit

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Phidata (Agents + Tools)**
- **Google Gemini 2.0 Flash API**
- **DuckDuckGo (Web Tool)**
- **Generative AI SDKs**
- **tempfile, mimetypes, dotenv**

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/agentic-video-summarizer.git
   cd agentic-video-summarizer
2. **Create and activate a virtual environment**
   python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies**
   pip install -r requirements.txt
   
5. **Add your API Key**
   Create a .env file in the root directory
   Add your Google API key:
   GOOGLE_API_KEY=your_api_key_here
   
7. **Usage**
   streamlit run app.py

