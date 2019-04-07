import os, sys 
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook',methods=['GET'])
def webhook():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "jerrymamo":
            return "Mismatched, Get Lost", 403
        return "What Are You Doing Here Man? You Were Not Supposed To Be here", 200

if __name__ == "__main__":
    app.run()
