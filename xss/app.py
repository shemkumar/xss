from urllib.parse import uses_relative
from flask import Flask,render_template,request, url_for, escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    
    user_input = request.args.get("input")
    # Sanitize user_input for safe display
    sanitized_user_input = escape(user_input) if user_input else ""

    # The original logic for user_input_temp was an attempt at sanitization but was flawed.
    # Instead of trying to sanitize, we should ensure proper escaping when rendering.
    # For demonstration, we'll just pass the escaped input.
    user_input_temp = sanitized_user_input

    # The hardcoded XSS payload condition is removed as it's a vulnerability itself.
    # If specific content needs to be displayed based on input, it should be constructed securely.
    
    return render_template('results.html',user_input=sanitized_user_input,user_input_temp=user_input_temp)

if __name__ == "__main__":
    app.run(debug=False)
