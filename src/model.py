import os
from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI
import openai


class Model:
    def __init__(self):
        load_dotenv()

    @staticmethod
    def google_gemini(transcript, prompt, extra=""):
        load_dotenv()
        genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-1.5-pro")
        try:
            response = model.generate_content(prompt + extra + transcript)
            return response.text
        except Exception as e:
            response_error = "⚠️ There is a problem with the API key or with python module."
            return response_error, e

    @staticmethod
    def openai_chatgpt(transcript, prompt, extra=""):
        load_dotenv()
        client = OpenAI(api_key=os.getenv("OPENAI_CHATGPT_API_KEY"))
        model = "gpt-3.5-turbo"
        message = [{"role": "system", "content": prompt + extra + transcript}]
        try:
            response = client.chat.completions.create(model=model, messages=message)
            return response.text
        except Exception as e:
            response_error = "⚠️ There is a problem with the API key or with python module."
            return f"{response_error} {str(e)}"

    @staticmethod
    def deepseek_chat(transcript, prompt, extra=""):
        from openai import OpenAI
        load_dotenv()
        try:
            # Configure client with DeepSeek API base and key
            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("DEEPSEEK_API_KEY"),
            )

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat:free",
                messages=[
                    {"role": "system", "content": prompt + extra + transcript}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return "⚠️ DeepSeek API error:", e