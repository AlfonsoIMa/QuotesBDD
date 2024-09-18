from flask              import Flask, render_template, redirect, url_for, g, request
from flask_sqlalchemy   import SQLAlchemy
from sqlalchemy.sql     import text
import logging, os, sqlite3

# because logging is better!
logging.basicConfig(format = '%(name)s@{asctime} : %(levelname)s : %(message)s',
                    datefmt = '%y%m%d_%H:%M',
                    level = logging.DEBUG)

# Creating a naming convention for db access
# db = SQLAlchemy()

# Starting the app
app = Flask(__name__)

# Establishing database connection and initializing
db_name = os.path.abspath('data/quotes.db')

def get_db():
    db = getattr(g, '_database', None)
    if(db is None):
        db = g._database = sqlite3.connect(db_name)
    return db

def query_db(query: str, args = (), one = False):
    c = get_db().execute(query, args)
    f = c.fetchall()
    get_db().commit()
    c.close()
    return (f[0] if f else None) if one else f

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if(db is not None):
        db.close()
    return 0

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add/author", methods = ['POST', 'GET'])
def add_author():
    if(request.method == 'POST'):
        authShort, authLong = [request.form['short_name'], request.form['full_name']]
        notification = None
        logging.debug((authShort, authLong))        

        # TODO - Return them into the page -> Wikipedia entry about them?
        # Insert only if both fields have been fulfilled, otherwise ask for them
        if(authShort and authLong):
            try:
                query_db('INSERT INTO author(display_name, full_name) VALUES (?, ?);', (authShort, authLong))
                notification = 'was sucessfully included!'
                return render_template('submit_author.html', notification = notification, authLong = authLong)
            except Exception as e:
                # TODO Beautify
                return f'<p>{e}</p>'
        else:
            # TODO
            pass
    else:
        return render_template('submit_author.html')

@app.route("/add/publisher", methods = ['POST', 'GET'])
def add_publisher():
    if(request.method == 'POST'):
        pubName = request.form['name']
        notification = None
        logging.debug(pubName)        

        # TODO - Return them into the page -> Wikipedia entry about them?
        # Insert only if both fields have been fulfilled, otherwise ask for them
        if(pubName):
            try:
                query_db('INSERT INTO publisher(name) VALUES (?);', (pubName,))
                notification = 'was sucessfully included!'
                return render_template('submit_publisher.html', notification = notification, pubName = pubName)
            except Exception as e:
                # TODO Beautify
                return f'<p>{e}</p>'
        else:
            # TODO
            pass
    else:
        return render_template('submit_publisher.html')

@app.route("/add/quote", methods = ['POST', 'GET'])
def add_quote():
    if(request.method == 'POST'):
        notification = None
        # TODO - logging.debug(pubName)        

        # TODO - Insert quote AND REDIRECT
        # TODO - Return them into the page -> Wikipedia entry about them?
        # Insert only if both fields have been fulfilled, otherwise ask for them
        if(pubName):
            try:
                query_db('INSERT INTO publisher(name) VALUES (?);', (pubName,))
                notification = 'was sucessfully included!'
                return render_template('submit_publisher.html', notification = notification, pubName = pubName)
            except Exception as e:
                # TODO Beautify
                return f'<p>{e}</p>'
        else:
            # TODO
            pass
    else:
        return render_template('submit_quote.html')
