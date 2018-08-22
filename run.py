import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/about")
def about():
    return render_template("about.htm", page_title="About")

@app.route('/contact')
def contact():
    return render_template("contact.htm", page_title="Contact")

@app.route('/careers')
def careers():
    return render_template("careers.htm", page_title="Careers")

if __name__ == '__main__':
   app.run(debug=True)     