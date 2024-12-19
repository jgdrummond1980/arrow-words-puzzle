from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key
openai.api_key = "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"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_puzzle():
    try:
        prompt = """
        Create an arrow words puzzle with clues and answers arranged in a grid format.
        Return the puzzle as a JSON object with 'grid' and 'clues'.
        """
response = openai.Completion.create(
    model="gpt-4",
    prompt="Create an arrow words puzzle with clues and answers arranged in a grid format. Return the puzzle as a JSON object with 'grid' and 'clues'.",
    max_tokens=500,
    temperature=0.7
)
        puzzle = response.choices[0].message["content"]
        return jsonify({"success": True, "puzzle": puzzle})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
