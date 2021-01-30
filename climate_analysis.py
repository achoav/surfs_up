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