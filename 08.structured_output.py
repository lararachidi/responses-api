# structured output

# pretty much the same between the Responses and Chat Completions APIs, the shape is just different.

# responses api using Pydantic model

from openai import OpenAI
from pydantic import BaseModel

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

response = client.responses.parse(
    model="gpt-4o-mini",
    input=[
        {"role": "system", "content": "Extract the event information."},
        {
            "role": "user",
            "content": "Alice and Bob are going to a science fair on Friday.",
        },
    ],
    text_format=CalendarEvent,
)

event = response.output_parsed
print(event.model_dump_json(indent=2))

# chat completions api using pydantic model

from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()

class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]

completion = client.beta.chat.completions.parse( # don't forget the beta here
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Extract the event information."},
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday."},
    ],
    response_format=CalendarEvent,
)

event = completion.choices[0].message.parsed
print(event.model_dump_json(indent=2))

### Notes ###
# Chat completions API documentation: https://platform.openai.com/docs/guides/structured-outputs?api-mode=chat
# Responses API documentation: https://platform.openai.com/docs/guides/structured-outputs?api-mode=responses