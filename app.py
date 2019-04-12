import os, sys 
from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook',methods=['GET'])
def webhook():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if request.args.get("hub.verify_token") == "jerrymamo":
            return "Matched", 200
        else:
            return "Did not Mathed", 403
    else:
        return "Not Requested For Webhook", 200





if __name__ == "__main__":
    app.run(debug = True,)
