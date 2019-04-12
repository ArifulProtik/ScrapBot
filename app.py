import os, sys 
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook')

def verifyToken():
    if request.args.get("hub.verify_token") == "jerry":
        return request.args.get("hub.challenge")
    else:
        "Didnt match"
def listenAndServe():
    if request.method == 'GET':
        return verifyToken()



if __name__ == "__main__":
    app.run(debug = True,)
