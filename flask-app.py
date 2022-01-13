#!/usr/bin/env python3

# File name: flask-app.py
# Description: Flask web application
# Author: Viktor Vodnev
# Date: 13-01-2022

import os
import psycopg2
from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, session
from sqlalchemy import create_engine

app = Flask(__name__)

def url():
    user = os.environ['POSTGRES_USER']
    host = os.environ['POSTGRES_HOST']
    port = int(os.environ['POSTGRES_PORT'])
    db = os.environ['POSTGRES_DB_NAME']
    passwd = os.environ['POSTGRES_PASSWORD']
    URL = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    return URL

Base = automap_base()
engine = create_engine(url())
Base.prepare(engine, reflect=True)
session = Session(engine)
Visitors = Base.classes.visitors


@app.route('/api/count/add', methods=["GET"])
def count_add():
    count = session.query(Visitors).first()
    count.value += 1
    session.commit()
    return '<h2 style="text-align: center;">Dziękujemy za odwiedzenie naszej strony internetowej!</h2>'


@app.route('/api/count', methods=["GET"])
def count_show():
    count = session.query(Visitors).first()
    return '<h2 style="text-align: center;">Liczba wyświetleń strony /api/count/add: <span style="color: #ff0000;">' + str(count.value) + '</span></h2>'
 
 
if __name__ == '__main__':
    app.run()