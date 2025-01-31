from flask import Flask, request, render_template_string
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__)

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# HTML template with Bootstrap styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>ETL Code Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f8f9fa; padding-top: 50px; }
        .container { max-width: 700px; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        textarea { resize: none; }
        pre { background-color: #f4f4f4; padding: 15px; border-radius: 5px; white-space: pre-wrap; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">ETL Code Generator</h1>
        <form method="POST">
            <div class="mb-3">
                <textarea name="user_input" class="form-control" rows="5" placeholder="Describe your ETL process..."></textarea>
            </div>
            <div class="text-center">
                <button type="submit" class="btn btn-primary">Generate Code</button>
            </div>
        </form>
        {% if generated_code %}
        <div class="mt-4">
            <h2 class="text-center">Generated Code:</h2>
            <pre class="bg-light p-3 border rounded">{{ generated_code }}</pre>
        </div>
        {% endif %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

def generate_etl_code(user_input):
    # Generate code using GPT-2
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=200,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )
    generated_code = tokenizer.decode(output[0], skip_special_tokens=True)
    
    # Improve formatting of generated code
    generated_code = generated_code.replace('S2', 'S3').replace('S1', 'CSV').replace('S4', 'S3').replace('S5', 'S3').replace('S6', 'S3')
    
    return generated_code

@app.route("/", methods=["GET", "POST"])
def index():
    generated_code = None
    if request.method == "POST":
        user_input = request.form["user_input"]
        generated_code = generate_etl_code(user_input)
    return render_template_string(HTML_TEMPLATE, generated_code=generated_code)

if __name__ == "__main__":
    app.run(debug=True)