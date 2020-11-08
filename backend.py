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
    movieData = pd.read_sql_query("SELECT * from movie", con)

    # close dbs

    return movieData.head(10).to_json(orient='records')

# @app.route('/movie/', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization','Access-Control-Allow-Origin'])
# def post_movie():
#     con = sqlite3.connect("movieData.sqlite")
#     cur = con.cursor()
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     req_data = request.get_json()
#     print("AA")
#     movieData = pd.read_sql_query("SELECT * from movie", con)

#     return movieData.head(10).to_json(orient='records')

@app.route("/movies/<id>", methods=["DELETE"])
def guide_delete(id):
    con = sqlite3.connect("movieData.sqlite")
    cur = con.cursor()

    cur.execute(f"DELETE FROM movie WHERE id='{id}'")
    con.commit()

    movieData = pd.read_sql_query("SELECT * from movie", con)

    return movieData.head(10).to_json(orient='records')

app.run()