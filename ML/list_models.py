from google import genai

# Replace with your API key
client = genai.Client(api_key="AIzaSyBiJ5UURhsoJc8Fzpp26Nnlj5yZZD1m4rA")

# List all available models
models = client.models.list()

# Print each model's name and supported actions
for m in models:
    print("Model Name:", m.name)
    print("Supported Actions:", m.supported_actions)

    print("-" * 40)
