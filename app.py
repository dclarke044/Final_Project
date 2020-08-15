
import numpy as np
import pandas as pd
 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import create_classes
from predict import getRating
from flask import request
from flask import url_for
import joblib

from config import username, password

#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/movies'
db = SQLAlchemy(app)
moviedata = create_classes(db)
migrate = Migrate(app, db)

model = joblib.load("./ML Models/rf.sav")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/home")
def home():
        return render_template('home.html')

@app.route("/models")
def models():
        return render_template('models.html')

@app.route("/rf", methods=['POST','GET'])
def rf():
        if request.method == 'POST':
                # print(request.form)
                year= request.form['inputYear']
                duration= request.form['inputDuration']
                budget= request.form['inputBudget']
                genre= request.form['inputGenre']
                director= request.form['inputDirector']
                test = [year, duration, budget, genre, director]
               
                # test = [2015, 150, 750000, "Comedy", "Tyler Perry"]
                #
                ratingResult= getRating(test)
                return redirect('/tableauyear')
        return render_template('rf.html')

@app.route("/rfresults", methods = ['POST', 'GET'])   
def rfresults():
        if request.method == 'POST':
                result = request.form
                print(result)
                year= request.form['inputYear']
                duration= request.form['inputDuration']
                budget= request.form['inputBudget']
                genre= request.form['inputGenre']
                director= request.form['inputDirector']
                test = [year, duration, budget, genre, director]
                

        return render_template("rfresults.html", ratingResult= getRating(test))

@app.route("/tableauyear")
def tableauyear():
        return render_template('tableauyear.html')

@app.route("/tableaugenre")
def tableaugenre():
        return render_template('tableaugenre.html')

@app.route("/tableaudirector")
def tableaudirector():
        return render_template('tableaudirector.html')

@app.route("/members")
def members():
        return render_template('members.html')

@app.route("/data-table")
def data():
        return render_template('data-table.html')

@app.route("/raw-data")
def data_pull():
        results = db.session.query(moviedata.index, moviedata.imdb_title_id, moviedata.title, moviedata.year, moviedata.genre, moviedata.duration, moviedata.country, moviedata.director, moviedata.production_company, moviedata.budget, moviedata.total_votes, moviedata.median_vote, moviedata.all18to29, moviedata.all30to44, moviedata.allover45, moviedata.males, moviedata.males18to29, moviedata.males30to44, moviedata.malesover45, moviedata.females, moviedata.females18to29, moviedata.females30to44, moviedata.femalesover45, moviedata.rating_class).all()
        # initialize dictionary 
        data = []
        for result in results:
                d = {"id":result[0], "imdb_title_id":result[1], "title" : result[2], "year" : result[3], "genre" : result[4], "duration" : result[5], "country" : result[6], "director" : result[7], "production_company" : result[8], "budget":result[9], "total_votes":result[10], "median_vote" : result[11], "all18-29" : result[12], "all30to44" : result[13], "allover45" : result[14], "males" : result[15], "males18to29" : result[16], "males30to44" : result[17], "malesover45":result[18], "females":result[19], "females18to29" : result[20], "females30to44" : result[21], "femalesover45" : result[22], "rating_class" : result[23]} 
                data.append(d)
        json_data = jsonify(data)
        return json_data

if __name__ == '__main__':
    app.run(debug=True)