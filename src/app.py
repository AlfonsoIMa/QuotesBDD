from flask              import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy   import SQLAlchemy
from sqlalchemy.sql     import text
import logging, os

# because logging is better!
logging.basicConfig(format = '%(name)s@{asctime} : %(levelname)s : %(message)s',
                    datefmt = '%y%m%d_%H:%M',
                    level = logging.DEBUG)

# Creating a naming convention for db access
db = SQLAlchemy()

# Starting the app
app = Flask(__name__)

# Establishing database connection and initializing
db_name                                      = str(os.path.abspath('data/quotes.db'))
app.config['SQLALCHEMY_DATABASE_URI']        = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# db.init_app(app)

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
    else:
        return render_template('submit_author.html')
