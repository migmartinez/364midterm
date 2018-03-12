###############################
####### SETUP (OVERALL) #######
###############################

## Import statements
# Import statements
import os
from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_script import Manager, Shell
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError # Note that you may need to import more here! Check out examples that do what you want to figure out what.
from wtforms.validators import Required, Length # Here, too
from flask_sqlalchemy import SQLAlchemy
import jinja2
import requests, json, operator
#from flask_sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, Date, Time
#from flask_sqlalchemy import relationship, backref


## App setup code
app = Flask(__name__)
app.debug = True
app.use_reloader = True

## All app.config values
app.config['SECRET_KEY'] = 'hard to guess string from me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lolcat123@localhost/book_of_betrayal'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## Statements for db setup (and manager setup if using Manager)
manager = Manager(app)
db = SQLAlchemy(app)

# Table
#name_names = db.Table('name')

######################################
######## HELPER FXNS (If any) ########
######################################

def get_or_create_name(db_session,namename):
    name = db_session.query(Name).filter_by(name=namename).first()
    name = Name(name=namename)
    db_session.add(name)
    db_session.commit()
    return name

def get_or_create_movie(db_session,moviename):
    movie_name = db_session.query(Movie).filter_by(name=moviename).first()
    movie_name = Movie(movie_name = moviename)
    db_session.add(movie_name)
    db_session.commit()
    return movie_name

def get_iterations():
    name_dict = {}
    names = db.session.query(Name.name)
    for name in names:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    return name_dict

def get_betrayal_leader():
    dictionary = get_iterations()
    leader = max(dictionary.items(), key=operator.itemgetter(1))
    return leader


##################
##### MODELS #####
##################

class Name(db.Model):
    __tablename__ = "names"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return "{} (ID: {})".format(self.name, self.id)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(64))

class LeaderBoard(db.Model):
    __tablename__ = "leaderboard"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),db.ForeignKey("names.name"))
    iterations = db.Column(db.Integer)

    def __repr__(self):
        return "{} has been mentioned {} times.".format(self.name, self.iterations)

###################
###### FORMS ######
###################

class NameForm(FlaskForm):
    name = StringField("Please enter your name.",validators=[Required()])
    submit = SubmitField('Submit')

class MovieRelForm(FlaskForm):
    movie = StringField("Enter your favorite movie.",validators=[Required()])
    submit = SubmitField('Submit')



#######################
###### VIEW FXNS ######
#######################

@app.route('/', methods=['POST', 'GET'])
def home():
    names = Name.query.all()
    form = NameForm() # User should be able to enter name after name and each one will be saved, even if it's a duplicate! Sends data with GET
    if form.validate_on_submit():
        get_or_create_name(db.session,form.name.data)
        return redirect(url_for('all_names'))
    return render_template('base.html',form=form)

@app.route('/names', methods=['GET', 'POST'])
def all_names():
    all_names = []
    names = Name.query.all()
    for n in names:
        name = Name.query.filter_by(name=n.name).first()
        all_names.append(n.name)
    return render_template('name_example.html',names=all_names)

@app.route('/leaderboards', methods=['GET', 'POST'])
#def leaderboard():
#   all_data = []
#    i = 0
#    names = Name.query.all()
#    for n in names:
#        i = i + 1
#        if n in names:
#            i = i + 1
#        all_data.append(tuple((n,i)))
def leaderboard():
    new = get_iterations()
    leader = get_betrayal_leader()
    return render_template('leaderboards.html', items=new, leader=leader)

@app.route('/movies', methods = ['GET', 'POST'])
def movie_suggestion():
    form = MovieRelForm()
    if form.validate_on_submit():
        get_or_create_movie(db.session, form.movie.data)
        return redirect(url_for('all_movies'))
    return render_template('movie_sugg.html', form=form)
def all_movies():
    all_movies = []
    movies = Movie.query.all()
    for m in movies:
        all_movies.append(m)
    return render_template('', items=all_movies)
def lookup(movie_title):
    params = {}
    params["s"] = movie_title
    params["type"] = movie
    resp = requests.get('')




## ERROR HANDLING ROUTES
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 500




## Code to run the application...

# Put the code to do so here!
# NOTE: Make sure you include the code you need to initialize the database structure when you run the application!
if __name__ == '__main__':
    db.create_all()
    manager.run()