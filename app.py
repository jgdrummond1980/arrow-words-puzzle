from flask import Flask, request, jsonify, render_template
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set your OpenAI API Key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found! Please set it in the environment variables.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_puzzle():
    try:
        prompt = "Create an arrow words puzzle with clues and answers arranged in a grid format. Return the puzzle as a JSON object with 'grid' and 'clues'."
        
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "engine" for older OpenAI versions
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )

        puzzle = response.choices[0].text.strip()
        return jsonify({"success": True, "puzzle": puzzle})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
