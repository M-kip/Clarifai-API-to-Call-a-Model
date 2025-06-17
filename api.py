import os
from openai import OpenAI
from dotenv import load_dotenv
# Load environment variables from a .env file
from pprint import pprint as pp
# Set the OpenAI API key from an environment variable
load_dotenv()
# Ensure you have the CLARIFAI_API_KEY set in your environment variables
if not os.getenv("CLARIFAI_API_KEY"):
    raise ValueError("CLARIFAI_API_KEY environment variable is not set.")
client = OpenAI(
    base_url="https://api.clarifai.com/v2/ext/openai/v1",
    api_key=os.getenv("CLARIFAI_API_KEY"),
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