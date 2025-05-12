# web search

# responses api 

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    tools=[{"type": "web_search_preview"}], # add tool here 
    input="What should I visit in Rome?"
)

print(response.output_text)

# chat completions api - only works with certain models (please check doc link below for updates):
# gpt-4o-search-preview
# gpt-4o-mini-search-preview 

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini-search-preview",
    web_search_options={}, # add tool here + things like user location, etc. 
    messages=[
        {
            "role": "user",
            "content": "What should I visit in Rome?",
        }
    ],
)

print(completion.choices[0].message.content)

### Notes ### 
# Chat completions API documentation: https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat 
# Responses API documentation: https://platform.openai.com/docs/guides/tools-web-search?api-mode=responses