import os
from google import genai
import gradio as gr
import time

# Load API key
client = genai.Client(api_key=os.getenv("AIzaSyBdhi3XfGH2cdh1s1MZb1OtuH6CdsDUPUE"))

def chat(message, history):
    try:
        time.sleep(1)  # avoid rate limit

        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=message[:200]   # limit tokens
        )

        return response.text

    except Exception as e:
        return f"❌ ERROR: {str(e)}"

demo = gr.ChatInterface(
    fn=chat,
    title="Blazeemaa AI 🤖",
    description="AI chatbot powered by Gemini"
)

demo.launch()
