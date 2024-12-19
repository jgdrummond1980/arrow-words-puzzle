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
