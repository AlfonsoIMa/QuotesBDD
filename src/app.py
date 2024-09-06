from flask import Flask, render_template, redirect, url_for, request
import logging

# because logging is better!
logging.basicConfig(format = '%(name)s@{asctime} : %(levelname)s : %(message)s',
                    datefmt = '%y%m%d_%H:%M',
                    level = logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add/author", methods = ['POST', 'GET'])
def add_author():
    if(request.method == 'POST'):
        authShort, authLong = [request.form['short_name'], request.form['full_name']]
        notification = None
        logging.debug((authShort, authLong))        

        # TODO - Add them to the database
        #      - Return them into the page -> Wikipedia entry about them?
        #      - Added!
        if(authShort and authLong):
            notification = 'was sucessfully included!'
            return render_template('submit_author.html', notification = notification, authLong = authLong)
    return render_template('submit_author.html')
