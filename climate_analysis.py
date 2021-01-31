#  9.1.3. Import Numpy and Pandas Dependencies
import numpy as np
import pandas as pd
# 9.1.3. Import Datetime Dependencies ###
import datetime as dt

# 9.1.3. Import Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import Session
import os

# 9.1.3. Import Flask
from flask import jsonify # <- `jsonify` instead of `json`
from flask import Flask

# 9.5.1. Setup the Database, function 'create_engine()' allows us to access and query our SQLite Database
app = Flask(__name__)
engine = create_engine(f"sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station

# 9.5.1. Create a session link from Python to our database with the following code:
session = Session(engine)

# 9.5.1. Setup Flask application called 'app'
app = Flask(__name__)
###############################################
# Very Important to run flask
# $env:FLASK_APP = "climate_analysis.py"
# flask run
###############################################

# 9.5.2. Create the Welcome Route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<h3>
    /api/v1.0/precipitation <br>
    /api/v1.0/stations <br>
    /api/v1.0/tobs <br>
    /api/v1.0/temp/start/end <br>
    ''')

# 9.5.3. Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

# 9.5.4. Stations Route
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# 9.5.5. Monthly Temperature Route - Quert for Dates and Temperature Observations last year
@app.route("/api/v1.0/tobs")
def tobs():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    tobs_data_list = list(np.ravel(tobs_data))
    return jsonify(tobs_data_list=tobs_data_list)

#9.5.6 Statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#################################################################################
# To get preciptation data type  http://127.0.0.1:5000/api/v1.0/precipitation
# To get stations data type http://127.0.0.1:5000/api/v1.0/stations
# To get monthly temperature type http://127.0.0.1:5000/api/v1.0/tobs
# To get start type http://127.0.0.1:5000/api/v1.0/temp/start/end
#################################################################################
# Define Main Behavior
if __name__=="__main__":
    app.run(debug=True)
