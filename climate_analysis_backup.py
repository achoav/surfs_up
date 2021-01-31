#!/usr/bin/env python
# coding: utf-8

# 9.1.3. Import Numpy and Pandas Dependencies
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

# Import Flask
from flask import Flask

#################################################
# Database Setup
#################################################

# 9.1.4. QLAlchemy Create Engine. Database setup
engine = create_engine("sqlite:///hawaii.sqlite")

# 9.1.4. SQLAlchemy Automap Base. Reflect an existing database into a new model
Base = automap_base()

# 9.1.4. SQLAlchemy Reflect tables using the function 'prepare()' establish schema and mappings
Base.prepare(engine, reflect=True)

# 9.1.4. Save references to each table: 'Measurement' and 'Station'. 
# Base.classes.<class name> give us access to all the classes
# 'Keys()' references all the names of the classes
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# 9.2.1. Retrieve the Precipitation Data
prev_year = dt.date(2017, 8, 23)
prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
results = []
results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

# 9.2.2. Save Query Results
df = pd.DataFrame(results, columns=['date','precipitation'])
df.set_index(df['date'], inplace=True)

# 9.2.3. Sort the DataFrame
df = df.sort_index()
#print(df.to_string(index=False))

# 9.2.5 Generate Summary of statistics
df.describe()

# 9.3.2. Determine the Most Active Stations
session.query(func.count(Station.station)).all()
session.query(Measurement.station, func.count(Measurement.station)).\
group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

# 9.3.3. Find Low, High and Average Temperatures
session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
filter(Measurement.station == 'USC00519281').all()

# 9.3.4. Create a query for Temperature Observations
results = session.query(Measurement.tobs).\
filter(Measurement.station == 'USC00519281').\
filter(Measurement.date >= prev_year).all()
#print(results)

# 9.3.4. Convert query into a dataframe
df = pd.DataFrame(results, columns=['tobs'])

# 9.3.4. Create a New Flask App Instance
app = Flask(__name__)

# 9.3.4. Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world'
export FLASK_APP=app.py
