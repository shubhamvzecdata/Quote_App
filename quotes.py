from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:root@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))

@app.route('/')
def index():
  result = Favquotes.query.all()
  return render_template('index.html', result=result)

@app.route('/about')
def about():
  return '<h1>Hello, World from about page.</h1>'

@app.route('/quotes')
def quotes():
  return render_template('quotes.html')

@app.route('/process',methods=['POST'])
def process():
  author = request.form['author']
  quote = request.form['quote']
  quotedata = Favquotes(author=author,quote=quote) 
  db.session.add(quotedata)
  db.session.commit()
  return redirect(url_for('index'))