from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True   
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://consistent:fitness@localhost:8889/consistent'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'mawsaysFinalProject'

#class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #username = db.Column(db.String(120), unique=True)
    #password = db.Column(db.String(120))
    #progress = db.relationship(Progress, backref='data')

    #def __init__(self, username, password):
        #self.username = username
        #self.password = password

class Activities(db.Model):
    activity_code = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(120))
    equipment = db.Column(db.String(120))
    zone = db.Column(db.String(2500))
    setting = db.Column(db.String(2500)) #chair/bench notes

    def __init__(self, exercise, equipment, zone, setting, pounds, num_set, reps):
        self.exercise = exercise
        self.equipment = equipment
        self.zone = zone
        self.setting = setting
    
#class Progress(db.Model):
    #date = db.Column(db.Date())
    #user = db.Column(db.Integer, db.ForeignKey('user.id'))
    #name of exercise = db.Column(db.String(2500), db.ForeignKey('activities.exercise')
    #pounds = db.Column(db.Integer) #make dials with 100s', 10's, 1's and .1 place
    #set = db.Column(db.Integer) #total of 3 sets
    #reps = db.column(db.Integer) # goal of 20 reps per set

    #def __init__(self, date, user, ):
        #self.username = username
        #self.password = password

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

if __name__ == '__main__':
    app.run()