from huggingface_hub import InferenceClient
client= InferenceClient(api_key='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')

messages = [
    {
        "role":"user",
        "content":" What is the capital of Russia?"
    }
]

stream = client.chat.completions.create(
    model="Qwen/Qwen2.5-Coder-32B-Instruct",
    messages=messages,
    max_tokens=200,
    stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")