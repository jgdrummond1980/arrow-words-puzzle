from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Set your OpenAI API Key as an environment variable or replace below.
openai.api_key = os.getenv("OPENAI_API_KEY", "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")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_puzzle():
    try:
        # Prompt for generating arrow word puzzles
        prompt = (
            "Create an arrow words puzzle with clues and answers arranged in a grid format. "
            "Return the puzzle as a JSON object with 'grid' (a 2D array) and 'clues' (a list of clues)."
        )

        # OpenAI API call
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )

        # Parse the response from OpenAI
        puzzle = response.choices[0].text.strip()
        return jsonify({"success": True, "puzzle": puzzle})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
