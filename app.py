from flask import Flask, request
from openai import OpenAI
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

@app.route("/reply", methods=["POST"])
def add_guide():
    input = request.json["input"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a pirate."},
            {"role": "user", "content": input},
        ]
    )
    return {
        "response" : response.choices[0].message.content
    }

@app.route("/audio", methods=["POST"])
def save_audio():
    input = request.files['audio']
    audio_name = input.filename
    input.save("audio/"+audio_name)
    # with open('audio/'+audio_name, 'w') as f:
    #     f.write(input.content)


