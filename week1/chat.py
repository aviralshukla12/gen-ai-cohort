from dotenv  import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are a ai assistent that specialized in maths.
Your task is to help the user with any maths related questions.
"""


client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system" , "content": system_prompt},
        {"role": "user" , "content": "Hey ther!"}    #zero shot promting
    ]
)
print(result.choices[0].message.content)