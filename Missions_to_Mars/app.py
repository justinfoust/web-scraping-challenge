###---------------------------------------------------------###
###   Web Scraping HW -- Mission to Mars                    ###
###   Justin Foust  --  01/11/2020  --  Data Boot Camp      ###
###---------------------------------------------------------###


from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/home")
def index():
    mars_info = mongo.db.mars.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/")
def scrape():
    mars_info = mongo.db.mars
    data = scrape_mars.scrape()
    mars_info.update(
        {},
        data,
        upsert=True
    )
    return redirect("/home", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)