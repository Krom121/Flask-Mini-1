import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/about")
def about():
    return render_template("about.htm")

@app.route('/contact')
def contact():
    return render_template("contact.htm")

@app.route('/careers')
def careers():
    return render_template("careers.htm")

if __name__ == '__main__':
   app.run(debug=True)     