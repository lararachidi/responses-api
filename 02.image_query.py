# images as an input
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv() 
client = OpenAI()

# responses api

response = client.responses.create(
    model="gpt-4o-mini",              
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text",  "text": "What's in this image?"},      
                {"type": "input_image", "image_url": ("https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
                )},
            ],
        }
    ],
)

print(response.output_text)

# chat completions api

from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{
        "role": "user",
        "content": [
            {"type": "text", "text": "What's in this image?"},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            },
        ],
    }],
)

print(response.choices[0].message.content)


### Notes ### 

# the shape of requests and the response objects differ between chat adn responses api
# Responses API documentation: https://platform.openai.com/docs/guides/images-vision?api-mode=responses
# Chat Completions API documentation: https://platform.openai.com/docs/guides/images-vision?api-mode=chat 