import os
from openai import OpenAI
from pprint import pprint as pp
# Set the OpenAI API key from an environment variable
client = OpenAI(
    base_url="https://api.clarifai.com/v2/ext/openai/v1",
    api_key="3ad9c142c609489a8c8341bea1ba17b8",
)
try:
    response = client.chat.completions.create(
    model="https://clarifai.com/gcp/generate/models/gemini-2_0-flash",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "Create a sample HSK 3 use available online resources ?",
        },
    ],
    temperature=0.7,
    stream=False, # stream=True also works, just iterator over the response
    )
    pp(response)
except Exception as e:
    print(f"An error occurred: {e}")
    if hasattr(e, 'response'):
        print(f"Response status code: {e.response.status_code}")
        print(f"Response content: {e.response.content.decode('utf-8')}")
    else:
        print("No response available.")