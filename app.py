from flask import Flask, jsonify
from flask_cors import CORS
#from collections import Iterable
import sqlite3
import json

def connector():
    conn = sqlite3.connect("tb2.db")
    cor = conn.cursor()
    return conn, cor
app = Flask(__name__)
CORS(app)



@app.route("/")
def hello_world():
    connect = connector()
    #cor.execute("insert into data(name, age) values(?,?)" ,( fname, age))
    conn = connect[0]
    cor = connect[1]
    cor.execute("""create table  if not exists data(id integer primary key unique, name char(20), age integer(3))""")
    conn.commit()
    cor.execute("select * from data")
    items = cor.fetchall()
    #return "lol"
    return jsonify(items)
    

@app.route("/<name>/<age>")
def take(name, age):
    conn = sqlite3.connect("tb2.db")
    cor = conn.cursor()
    cor.execute("insert into data(name, age) values(?,?)" ,( name, age))
    cor.execute("select * from data")
    items = cor.fetchall()
    conn.commit()
    return jsonify(items)

@app.route("/<id>")
def remove(id):
    conn = sqlite3.connect("tb2.db")
    cor = conn.cursor()
    cor.execute("delete from data where id =?",(id,))
    cor.execute("select * from data")
    items = cor.fetchall()
    conn.commit()
    return jsonify(items)

if __name__ == "__main__":
    app.run(debug=True)
    