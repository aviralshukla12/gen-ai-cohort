from google import genai
from google.genai import types


# Only run this block for Gemini Developer API
client = genai.Client(api_key='AIzaSyCTO1kkAfQGXpNcZltFbUsMtEQ8mSE2Ths')

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='Why is the sky blue?'
)
print(response.text)