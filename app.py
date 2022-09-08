#Dependencies
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as soup
import scraping

# Setup Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app" #Tells Py that app will cnnct to mongo using URI
mongo = PyMongo(app) #this is the URI to connect app to mongo

# setup homepage
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

# setup scraping route
# update_one syntax: .update_one(query_parameter, {"$set": data}, options)
# "$set:" = document will be modified with the data in question
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# Run Flask
if __name__ == "__main__":
    app.run()



































