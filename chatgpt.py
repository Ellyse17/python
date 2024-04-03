import openai

openai.api_key = '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'

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )
    return response.choices[0].text.strip()

# Example usage:
print(chat_with_gpt3("Translate the following English text to French: '{}'\n".format("Hello, world")))
