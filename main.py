from flask import Flask, request, redirect, render_template, session, flash
#from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
#app.config['DEBUG'] = True   
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:mbadded@localhost:8889/blogz'
#app.config['SQLALCHEMY_ECHO'] = True
#db = SQLAlchemy(app)
#app.secret_key = 'mawsaysFinalProject'

#class User(db.Model):

@app.route('/', methods=['POST', 'GET'])
def index(): 
    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['username'] = username
            flash("Logged in")
            print(session)
            return redirect('/newpost')
        else:
            flash('User password incorrect, or user does not exist', 'error')

    return render_template('login.html')

if __name__ == '__main__':
    app.run()