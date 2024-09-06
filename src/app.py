from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add/author")
def add_author():
    return render_template('submit_author.html')
