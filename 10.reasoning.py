# reasoning 

# reasoning models think before they answer, producing a long internal chain of thought before responding to the user. 
# reasoning parameter: More effort = more tokens, latency, and cost, but better reasoning.
# Similar between the two APIs: 
# for chat completions api: use `reasoning_effort`` 
# for responses api: use `reasoning.effort` 

# responses api 

from openai import OpenAI

client = OpenAI()

prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.responses.create(
    model="o4-mini",
    reasoning={"effort": "low"}, # set reasoning parameter 
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.output_text)

# chat completions api 

from openai import OpenAI

client = OpenAI()

prompt = """
Write a bash script that takes a matrix represented as a string with 
format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.
"""

response = client.chat.completions.create(
    model="o4-mini",
    reasoning_effort="low",
    messages=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)

### Notes ###
# Chat completions API documentation: https://platform.openai.com/docs/guides/reasoning?api-mode=chat
# Responses API documentation: https://platform.openai.com/docs/guides/reasoning?api-mode=responses