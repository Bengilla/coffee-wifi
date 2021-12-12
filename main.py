"""
On day 66, we create an API that serves data on cafes with wifi and good coffee. Today, you're going to use the data from that project to build a fully-fledged website to display the information.

Included in this assignment is an SQLite database called cafes.db that lists all the cafe data.

Using this database and what you learnt about REST APIs and web development, create a website that uses this data. It should display the cafes, but it could also allow people to add new cafes or delete cafes.

For example, this startup in London has a website that does exactly this:

https://laptopfriendly.co/london
"""

import sqlite3
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.String, nullable=False)
    has_toilet = db.Column(db.String, nullable=False)
    has_wifi = db.Column(db.String, nullable=False)
    can_take_calls = db.Column(db.String, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)


@app.route("/")
def main():
    all_cafe = db.session.query(Cafe).all()
    return render_template("index.html", all_cafe=all_cafe)

if __name__ == "__main__":
    app.run(debug=True)