from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client= OpenAI (
    api_key="AIzaSyBMUuBGS9q-YLAkVTtPctKA7YxtT7v0hX4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#zero shot is directly giving the prompt to the model
SYSTEM_PROMPT="You should only and only science related question. If the user ask anything else say you dont know anything and your name is alexa"

response= client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
          {"role": "system", "content": SYSTEM_PROMPT },
          { "role": "user", "content": "hey there, can you tell me a joke about planets?"}
        ]
)

print(response.choices[0].message.content)

