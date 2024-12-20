from openai import OpenAI
from flask import Flask, render_template, request
import json

client = OpenAI()

app = Flask(__name__, template_folder="templates", static_url_path="", static_folder="static")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def get_palette():
    messages = [
        {
            "role": "system",
            "content": "You are a color palette generating assistant tasked with generating a color palette that "
                       "fits the mood, theme, or instructions the user is asking for. "
                       "Generate between 2-6 colors per prompt unless stated otherwise. "
                       "Desired Format: JSON array of hexadecimal color codes."
        },
        {
            "role": "user",
            "content": "a swampy, green forest"
        },
        {
            "role": "assistant",
            "content": "[\"#7F755F\", \"#6C6783\", \"#24342A\", \"#00576F\"]"
        },
        {
            "role": "user",
            "content": "neon city at dusk."
        },
        {
            "role": "assistant",
            "content": "[\"#7DF9FF\", \"#7DF9FF\", \"#32CD32\", \"#8A2BE2\", \"#191970\"]"
        },
        {
            "role": "user",
            "content": "colors of the italian flag"
        },
        {
            "role": "assistant",
            "content": "[\"#009246\", \"#FFFFFF\", \"#CE2B37\"]"
        }
    ]
    data = request.get_json()
    prompt = data.get("prompt")
    messages.append({
        "role": "user",
        "content": prompt
    })
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    colors = json.loads(response.choices[0].message.content)
    return {"colors": colors}


if __name__ == "__main__":
     app.run(debug=True)
