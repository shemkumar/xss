from urllib.parse import uses_relative
from flask import Flask,render_template,request, url_for, escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    
    user_input = request.args.get("input")
    # Escape user_input to prevent XSS. Jinja2's autoescaping is usually sufficient,
    # but explicit escaping here ensures it's always treated as safe text.
    # The previous manual sanitization was insufficient and bypassable.
    escaped_user_input = escape(user_input) if user_input else ""
    
    # The user_input_temp variable and its associated logic are removed
    # as they provided a false sense of security and are not needed with proper escaping.
    return render_template('results.html',user_input=escaped_user_input)

if __name__ == "__main__":
    app.run(debug=False)
