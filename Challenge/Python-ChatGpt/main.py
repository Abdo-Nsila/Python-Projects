import openai

openai.api_key = "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"

completion = openai.Completion.create(
    engine='gpt-3.5-turbo',
    messages=[{"role": "user", "content": "Hello Bro"}]
)

response = completion.choices[0].message.content 
print(response)