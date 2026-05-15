from urllib.parse import uses_relative
from flask import Flask,render_template,request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    
    user_input = request.args.get("input")
    # Remove the problematic XSS payload logic
    # Jinja2 auto-escapes by default, so direct rendering of user_input is safe
    # unless |safe or Markup() is explicitly used in the template.
    # The original logic attempted to sanitize but introduced a hardcoded payload.
    # We will rely on Jinja2's default auto-escaping.
    
    return render_template('results.html',user_input=user_input)

if __name__ == "__main__":
    app.run(debug=False)
