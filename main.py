from flask import Flask, request, redirect, render_template, session, flash
#from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True   
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://consistent:fitness@localhost:8889/consistent'
#app.config['SQLALCHEMY_ECHO'] = True
#db = SQLAlchemy(app)
#app.secret_key = 'mawsaysFinalProject'

#class User(db.Model):
    #id
    #username
    #password

#class Exercise(db.Model):
    #id - num
    #name of exercise - string
    #lbs (100's, 10's, 1's place on individual dials)
    #equipment
    #setting (chair, bench)

#class Progress(db.Model):
    #date
    #user
    #name of exercise
    #equipment
    #lbs

@app.route('/', methods=['POST', 'GET'])
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

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/lift', methods=['POST', 'GET'])
def lift():
    return render_template('lift.html')

if __name__ == '__main__':
    app.run()