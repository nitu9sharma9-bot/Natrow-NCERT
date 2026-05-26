from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("AIzaSyADKFmyS3u6vk0Y7r2xy7nFKCvUaSasKS4")

print("KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

client = genai.Client(api_key=api_key)

try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Hello"
    )

    print(response.text)

except Exception as e:
    print("ERROR:")
    print(e)