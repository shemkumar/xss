from urllib.parse import uses_relative
from flask import Flask,render_template,request, url_for
from markupsafe import escape
import os

app = Flask(__name__)

@app.route('/')
def index():
    return regnder_template('index.html')


@app.route('/result')
def result():
    
    user_input = request.args.get("input")
    # Escape user_input immediately to prevent XSS
    escaped_user_input = escape(user_input)
    
    # The original logic for user_input_temp was flawed and introduced a guaranteed XSS.
    # It's removed to prevent this vulnerability. All user input should be escaped.
    # If specific HTML tags are required, a robust HTML sanitization library should be used.
    user_input_temp = user_input # Assign original user_input to user_input_temp
    
    # Escape user_input_temp before passing it to the template
    escaped_user_input_temp = escape(user_input_temp)

    return render_template('results.html',user_input=escaped_user_input,user_input_temp=escaped_user_input_temp)

if __name__ == "__main__":
    app.run(debug=False)
