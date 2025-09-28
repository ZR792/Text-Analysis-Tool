import os
import google.generativeai as genai
from dotenv import load_dotenv
import time
from config import SUMMARY_MODEL

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini:
genai.configure(api_key=API_KEY)

# Reusable function for text summarization:
def summarize_text(text):
    try:
        model = genai.GenerativeModel(SUMMARY_MODEL)  
        response = model.generate_content(f"Summarize this text:\n{text}")
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Error Handling & Rate Limiting:
def safe_api_call(text, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return summarize_text(text)
        except Exception as e:
            print(f"Error occurred: {e}, retrying... ({attempt+1}/{retries})")
            time.sleep(delay)
    return "API failed after retries."

# -----------------------
# TAKING USER INPUT:
# -----------------------
if __name__ == "__main__":
    user_text = input("Enter the text you want to summarize: ")
    result = safe_api_call(user_text)
    print("\n--- Summary ---")
    print(result)
