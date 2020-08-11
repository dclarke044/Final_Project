
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

from config import username, password

#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/movies'
db = SQLAlchemy(app)
moviedata = create_classes(db)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bar")
def bar():
        return render_template('barchart.html')

@app.route("/bubble")
def bubble():
        return render_template('bubblechart.html')

@app.route("/map")
def map():
        return render_template('impactmap.html')

@app.route("/data-table")
def data():
        return render_template('data-table.html')

@app.route("/raw-data")
def data_retrieval():
        results = db.session.query(moviedata.id, moviedata.imdb_title_id, moviedata.title, moviedata.year, moviedata.genre, moviedata.duration, moviedata.country, moviedata.director, moviedata.production_company, moviedata.budget, moviedata.total_votes, moviedata.median_vote, moviedata.18andunder, moviedata.under30, moviedata.under45, moviedata.males, moviedata.malesunder18, moviedata.malesunder30, moviedata.malesunder45, moviedata.females, moviedata.femalesunder18, moviedata.femalesunder30, moviedata.femalesunder45, moviedata.rating_class).all()
        # initialize dictionary 
        data = []
        for result in results:
                d = {"id":result[0], "imdb_title_id":result[1], "title" : result[2], "year" : result[3], "genre" : result[4], "duration" : result[5], "country" : result[6], "director" : result[7], "production_company" : result[8], "budget":result[9], "total_votes":result[10], "median_vote" : result[11], "18andunder" : result[12], "under30" : result[13], "under45" : result[14], "males" : result[15], "malesunder18" : result[16], "malesunder30" : result[17], "malesunder45":result[18], "females":result[19], "femalesunder18" : result[20], "femalesunder30" : result[21], "femalesunder45" : result[22], "rating_class" : result[23]} 
                data.append(d)
        json_data = jsonify(data)
        return json_data

if __name__ == '__main__':
    app.run()