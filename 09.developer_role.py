# new developer role 

# helps provide granular control without making your system prompt too big
# Responses API: use the key-value “instructions” instead of passing separate “role: system” or “role: developer” messages

from openai import OpenAI

client = OpenAI()

# responses api option 1: using instructions parameter 

response = client.responses.create(
    model="gpt-4o-mini",
    instructions="Talk like a pirate.", # this is your "system-like" guardrail
    input="Are semicolons optional in JavaScript?",
)

print(response.output_text)


# responses api option 2: (closer to what was done with the completions api)

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user", "content": "Are semicolons optional in JavaScript?"},
    ],
)

print(response.output_text)

# Note - don’t try to include "role": "system" in the input array --> any “system” entries will just be demoted to developer‐level.

# chat completions api 

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
    ]
)

print(completion.choices[0].message.content)

# chain of command: assistant will NOT speak pirate-style, because system > developer:
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",    "content": "Don't talk like a pirate."},
        {"role": "developer", "content": "Talk like a pirate."},
        {"role": "user",      "content": "Are semicolons optional in JavaScript?"},
    ]
)
print(completion.choices[0].message.content) # doesnt talk like a pirate 


### Notes ###
# Chain of command article: https://model-spec.openai.com/2025-02-12.html#chain_of_command
# Documentation chat completions api: https://platform.openai.com/docs/guides/text?api-mode=chat 
# Documentation responses api: https://platform.openai.com/docs/guides/text?api-mode=responses  
# Source: https://community.openai.com/t/system-prompt-in-responses-api/1144116 