from openai import OpenAI
from flask import Flask, render_template, request
import ast

client = OpenAI()

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a color palette generating assistant tasked with generating a color palette that "
#                        "fits the mood, theme, or instructions the user is asking for. "
#                        "Generate between 2-6 colors per prompt unless stated otherwise. "
#                        "Desired Format: JSON array of hexadecimal color codes."
#         },
#         {
#             "role": "user",
#             "content": "a swampy, green forest"
#         },
#         {
#             "role": "system",
#             "content": "['#7F755F', '#6C6783', '#24342A', '#00576F']"
#         },
#         {
#             "role": "user",
#             "content": "neon city at dusk."
#         },
#         {
#             "role": "system",
#             "content": "['#7DF9FF', '#7DF9FF', '#32CD32', '#8A2BE2', '#191970]"
#         },
#         {
#             "role": "user",
#             "content": "colors of the italian flag"
#         },
#         {
#             "role": "system",
#             "content": "['#009246', '#FFFFFF', '#CE2B37']"
#         },
#         {
#             "role": "user",
#             "content": "colors of the chicago bulls"
#         }
#     ]
# )
#
# print(ast.literal_eval(completion.choices[0].message.content))
