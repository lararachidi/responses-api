# stream query

from openai import OpenAI
client = OpenAI()

# responses api documentation

from openai import OpenAI
client = OpenAI()

stream = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for event in stream:
    print(event)


# chat completions api 

from openai import OpenAI
client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk)
    print(chunk.choices[0].delta)
    print("****************")

### Notes ### 

#  comparison: the shape of the request and the type of objects you pull deltas out of that differ
# Responses API documentation: https://platform.openai.com/docs/guides/streaming-responses?api-mode=responses
# Chat Completions API documentation: https://platform.openai.com/docs/guides/streaming-responses 