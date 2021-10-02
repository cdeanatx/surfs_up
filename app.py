from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)
@app.route('/')

def welcome():
    return(
        '''
        Welcome to the Climate Analysis API!</br></br>
        Available Routes:</br></br>
        /api/v1.0/precipitation</br>
        /api/v1.0/stations</br>
        /api/v1.0/tobs</br>
        /api/v1.0/temp/start/end</br>
        ''')