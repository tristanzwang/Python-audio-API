from flask import Flask, request
from openai import OpenAI
from dotenv import load_dotenv
import os
from supabase import create_client, Client

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
supabase_key = os.getenv("SUPABASE_API_KEY")

client = OpenAI(api_key=api_key)
client1 = create_client("https://tymbjgfnqijjehcyyynr.supabase.co", supabase_key)

iden = 1

@app.route("/reply", methods=["POST"])
def add_guide():
    global iden
    input = request.json["input"]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a pirate."},
            {"role": "user", "content": input},
        ]
    )
    output = response.choices[0].message.content
    client1.table('ChatGPT').insert({"id": iden, "input": input, "output": output}).execute()
    iden = iden+1
    return {
        "response" : output
    }

@app.route("/audio", methods=["POST"])
def save_audio():
    input = request.files['audio']
    audio_name = input.filename
    input.save("audio/"+audio_name)