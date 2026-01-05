from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client= OpenAI (
    api_key="AIzaSyBMUuBGS9q-YLAkVTtPctKA7YxtT7v0hX4",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

#few shot is directly giving the prompt to the model and few examples to the model  
SYSTEM_PROMPT="""You should only and only coding related question. If the user ask anything else say you dont know anything and your name is alexa

Output
{{
    "code": "string" or null,
    "iscodingquestion": boolean
}}


Examples:
    Q: Can you explain me about love?
    A: {{ "code": null, "iscodingquestion": false }}

    
    Q: Hey, write a code to add two numbers in python,.
    A: {{ "code": "def add(a,b) :
                return a + b", "iscodingquestion": true }}
    
    """
response= client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
          {"role": "system", "content": SYSTEM_PROMPT },
          { "role": "user", "content": "hey there, can you give me the code to add n numbers in python?"}
        ]
)

print(response.choices[0].message.content)

