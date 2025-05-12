# file search

# upload the file to the File api 

import requests
from io import BytesIO
from openai import OpenAI
import textwrap

client = OpenAI()

def create_file(client, file_path):
    if file_path.startswith("http://") or file_path.startswith("https://"):
        # Download the file content from the URL
        response = requests.get(file_path)
        file_content = BytesIO(response.content)
        file_name = file_path.split("/")[-1]
        file_tuple = (file_name, file_content)
        result = client.files.create(
            file=file_tuple,
            purpose="assistants"
        )
    else:
        # Handle local file path
        with open(file_path, "rb") as file_content:
            result = client.files.create(
                file=file_content,
                purpose="assistants"
            )
    print(result.id)
    return result.id

# Replace with your own file path or URL
file_id = create_file(client, "https://cdn.openai.com/API/docs/deep_research_blog.pdf")

# create vector store 

vector_store = client.vector_stores.create(
    name="lara's vs'"
)
print(vector_store.id)

# check the vector store: https://platform.openai.com/storage/vector_stores/vs_680e3ae71fbc819193692ab7737b33fc

# add the file to the vector store using file id

result = client.vector_stores.files.create(
    vector_store_id=vector_store.id,
    file_id=file_id
)
print(result)

# check status 

result = client.vector_stores.files.list(
    vector_store_id=vector_store.id
)
print(result)

# check the vector store: https://platform.openai.com/storage/vector_stores/vs_680e3ae71fbc819193692ab7737b33fc

# file search tool

from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o",
    input="What is deep research by OpenAI?",
    tools=[{
        "type": "file_search",
        "vector_store_ids": ["vs_680e3ae71fbc819193692ab7737b33fc"], # add your vector store ID
        "max_num_results": 3, # play with the parameters
    }]
)
print(response)
print(textwrap.fill(response.output_text, width=80))

# directly query the vs using similarity search 

results = client.vector_stores.search(
    vector_store_id=vector_store.id,
    query="What is deep research by OpenAI?",
)

print(results.model_dump_json(indent=2))

### Notes ###
# Source: https://github.com/daveebbelaar/ai-cookbook/blob/main/models/openai/05-responses/07-file-search.py
# Responses API documentation https://platform.openai.com/docs/guides/tools-file-search
# Documentation on how to store files: https://platform.openai.com/storage/files/ 
# Documentation on how to create a vector store: https://platform.openai.com/storage/vector_stores 