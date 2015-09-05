from flask import Flask, render_template
from os import environ
from . import app

from .database import URL, session

from flask import request

#app = Flask(__name__)

@app.route("/")
@app.route("/save_url", methods=["POST"])

def save_url():
    return repr(request.data) 
    #session.add(url)
    session.commit()
    
    
    #return "URL saved! Type /urls to retrieve a list of all saved URLs."
    

#def say_hi():
    #print "URL Saved! Type /urls to retreive the list of all saved URLS."
    #print (app.config["DATABASE_URI"])
    
    #print request.data or request.form
    
   # return "Woo hoo! URL saved!"

    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))