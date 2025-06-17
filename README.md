# 🤖 Clarifai + OpenAI Chat Completion Example

This is a Python script demonstrating how to use **Clarifai's integration with OpenAI models** to generate chat completions using an external model like **Gemini 2.0 Flash**.

## 📦 Requirements

- Python 3.7+
- `openai` package
- Internet access
- A valid API key for Clarifai's OpenAI integration

## 🔧 Setup

1. **Install dependencies**  
   Install the `openai` package if you haven't already:

   ```bash
   pip install openai
   2. **Set your API key**  
      Export your Clarifai API key as an environment variable:

      ```bash
      export CLARIFAI_PAT=your_clarifai_pat_here
      ```

   3. **Run the script**  
      Execute the Python script to generate a chat completion:

      ```bash
      python clarifai_openai_chat.py
      ```

   4. **Customize the model**  
      You can change the model used by modifying the `model_id` variable in the script.