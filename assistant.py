from ollama import chat

response = chat(
    model='llama3.2:1b',
    messages=[
        {
            'role': 'user',
            'content': 'Namaste! Hindi mein batao: tum kaun ho aur tum kya kar sakte ho?'
        }
    ]
)

print("\nAI:", response.message.content)