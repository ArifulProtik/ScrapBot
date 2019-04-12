import os, sys 
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook')

def verifyToken(req):
    if req.args.get("hub.verify_token") == "jerry":
        return req.arhs.get("hub.challenge")
    else:
        "Didnt match"
def listenAndServe():
    if request.method == 'GET':
        return verifyToken(request)



if __name__ == "__main__":
    app.run(debug = True,)
