import pandas as pd
import sqlite3
import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/movies', methods=['GET'])
def api_all():
    con = sqlite3.connect("movieData.sqlite")
    cur = con.cursor()
    movieData = pd.read_sql_query("SELECT * from movie limit 10", con)

    con.close()

    return movieData.to_json(orient='records')

@app.route("/movies/<id>", methods=["DELETE"])
def guide_delete(id):
    con = sqlite3.connect("movieData.sqlite")
    cur = con.cursor()

    cur.execute(f"DELETE FROM movie WHERE id='{id}'")
    con.commit()

    movieData = pd.read_sql_query("SELECT * from movie limit 10", con)

    con.close()

    return movieData.to_json(orient='records')

app.run()