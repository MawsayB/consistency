from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi
import random 

app = Flask(__name__)
app.config['DEBUG'] = True   
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://consistent:fitness@localhost:8889/consistent'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'mawsaysFinalProject'

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
    #date = db.Column(DATE)
    #zone = db.Column(db.String(2500)
    #exercise = db.Column(db.String(2500), db.ForeignKey('activities.exercise')
    #pounds = db.Column(db.Integer) #make dials with 100s', 10's, 1's and .1 place
    #set = db.Column(db.Integer) #total of 3 sets
    #reps = db.column(db.Integer) # goal of 20 reps per set

    #def __init__(self, date, zone, exercise, pounds, set, reps):
        #self.zone = zone
        #self.password = password

@app.route('/analyze', methods=['POST', 'GET'])
def analyze():
     return render_template('analyze.html')

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect('/lift')         
    else:
        return render_template('index.html')

@app.route('/lift', methods=['POST', 'GET'])
def lift():
     return render_template('zone.html')

@app.route('/measure', methods=['POST', 'GET'])
def measure():
     return render_template('measure.html')

if __name__ == '__main__':
    app.run()