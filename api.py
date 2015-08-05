from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/save_url", methods=["POST"])
def say_hi():
    print "URL Saved! Type /urls to retreive the list of all saved URLS."
    return "Woo hoo! URL saved!"

    
if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))