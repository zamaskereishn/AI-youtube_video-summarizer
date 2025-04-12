

🎥 AI Video Summarizer & Timestamp Generator

 ![image](https://github.com/user-attachments/assets/02a128e1-ab34-4b00-b2c2-76541b7e11ff)

📝 Overview

This project is an AI-powered tool built to summarize YouTube videos and extract key timestamps. It uses advanced large language models (LLMs) like Google Gemini, OpenAI ChatGPT, and DeepSeek to generate concise summaries and structured breakdowns, helping users grasp video content without watching the entire thing.

✨ Features

Automatic summarization of YouTube videos using cutting-edge LLMs.

Timestamp generation for key moments in the video.

Uses youtube-transcript-api to extract video transcripts.

Allows users to choose between AI models (Gemini, ChatGPT, DeepSeek).

Saves time by delivering key insights quickly and effectively.

Built-in clipboard copy functionality for all generated content.

Transcript download support.

Getting Started

✅ Prerequisites

Python 3.10 or higher

API Keys for at least one supported LLM (Gemini, OpenAI, or DeepSeek)

💻 Installation

1) Clone the repository:
```
git clone https://github.com/zamaskereishn/AI-youtube_video-summarizer.git
```

Navigate into the project:
```
cd ai-video-summarizer-and-timestamp-generator-LLM-p
```
Install dependencies:
```
pip install -r requirements.txt
```
Create a .env file and add your API key(s):
```
GOOGLE_GEMINI_API_KEY="your-gemini-key"
OPENAI_CHATGPT_API_KEY="your-openai-key"
DEEPSEEK_API_KEY="your-deepseek-key"
```
Only one API key is needed to run the app, but you can add multiple to enable model switching.

▶️ Run the App
```
streamlit run app.py
```

🙏 Acknowledgments

Google Gemini

OpenAI ChatGPT

DeepSeek

Siddharth Kamble
