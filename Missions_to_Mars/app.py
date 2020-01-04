from flask import Flask, render_template, redirect
import pymongo
import scape_mars

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route("/")
def index():


@app.route("/scrape")
def scrape():
    data = scape_mars.scrape()
    