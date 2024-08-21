from openai import OpenAI
import ast

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a color palette generating assistant tasked with generating a color palette that "
                       "fits the mood, theme, or instructions the prompt is asking for. "
                       "Generate between 2-6 colors per prompt. "
                       "Desired Format: JSON array of hexadecimal color codes."
        },
        {
            "role": "user",
            "content": "a swampy, green forest"
        },
        {
            "role": "system",
            "content": "['#7F755F', '#6C6783', '#24342A', '#00576F']"
        },
        {
            "role": "user",
            "content": "a beautiful sunset at the beach."
        }
    ]
)

print(ast.literal_eval(completion.choices[0].message.content))
