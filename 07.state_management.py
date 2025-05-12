# Managing the conversation state

# Chat Completions: You have to manage conversation state yourself
# Responses: has previous_response_id to help you with long-running conversations
# Note: if you don’t want OpenAI to store the conversation, set store=False

# responses api - manually construct a past conversation

from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "user", "content": "knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
)

print(response.output_text)

# responses api - manually manage conversation state

from openai import OpenAI

client = OpenAI()

history = [
    {
        "role": "user",
        "content": "tell me a joke"
    }
]

response = client.responses.create(
    model="gpt-4o-mini",
    input=history,
    store=False
)

print(response.output_text)

# add the response to the conversation
history += [{"role": el.role, "content": el.content} for el in response.output]

history.append({ "role": "user", "content": "tell me another" })

second_response = client.responses.create(
    model="gpt-4o-mini",
    input=history,
    store=False
)

print(second_response.output_text)


# openapis for conversation state 

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)
print(response.output_text)

second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input=[{"role": "user", "content": "explain why this is funny."}],
)
print(second_response.output_text)

# chat completions api - manually construct past conversation

from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
)

print(response.choices[0].message.content)


# chat completions api - manually manage conversation state 

from openai import OpenAI

client = OpenAI()

history = [
    {
        "role": "user",
        "content": "tell me a joke"
    }
]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=history,
)

print(response.choices[0].message.content)

history.append(response.choices[0].message)
history.append({ "role": "user", "content": "tell me another" })

second_response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=history,
)

print(second_response.choices[0].message.content)


### Notes ###
# Chat completions api documentation: https://platform.openai.com/docs/guides/conversation-state?api-mode=chat#openai-apis-for-conversation-state
# Responses api documentation: https://platform.openai.com/docs/guides/conversation-state?api-mode=responses#openai-apis-for-conversation-state 
