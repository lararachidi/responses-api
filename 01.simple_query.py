# simple query comparing the chat completions vs responses api 

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()  
client = OpenAI() 

# responses api
# instead of wrapping everything in a messages array, you can now use a simple input string

response = client.responses.create(
    model="gpt-4o-mini", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text) # easier to get the output with typed response object with its own id

# chat completions api

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn.",
        }
    ],
)

print(response.choices[0].message.content)


### Notes ####

# Instead of a message, you receive a typed response object with its own id.
# Responses are stored by default. Chat completions are stored by default for new accounts.
# To disable storage when using either API, set store: false.
# Documentation: https://platform.openai.com/docs/guides/responses-vs-chat-completions 