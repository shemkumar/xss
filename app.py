from urllib.parse import uses_relative
from flask import Flask,render_template,request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def result():
    
    user_input = request.args.get("input")
    # Escape user_input immediately to prevent XSS
    escaped_user_input = escape(user_input)
    
    # The original logic for user_input_temp seems to be an attempt at sanitization
    # or a demonstration of a bypass. Given the finding, it's safer to escape this as well.
    # If the intent was to allow some HTML, a robust HTML sanitization library should be used.
    # For now, we'll escape it to prevent XSS.
    user_input_temp = user_input.lower()
    user_input_temp = user_input_temp.replace("script","")
    if (("img" in user_input_temp) and ("alert" in user_input_temp or "onerror" in user_input_temp) and ("<" in user_input_temp) and (">" in user_input_temp)):
        
        user_input_temp =  '<img src =q onerror=prompt("root@localhost{Byp4ss_Sanitiz3r_123}")>'
    
    # Escape user_input_temp before passing it to the template
    escaped_user_input_temp = escape(user_input_temp)

    return render_template('results.html',user_input=escaped_user_input,user_input_temp=escaped_user_input_temp)

if __name__ == "__main__":
    app.run(debug=False)
