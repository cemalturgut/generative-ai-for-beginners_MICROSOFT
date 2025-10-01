# smoke_test_gemini.py
import os
from google import genai

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])
resp = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Merhaba Gemini! Kısaca kendini tanıt."
)
print(resp.text)
