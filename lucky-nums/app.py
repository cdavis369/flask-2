from flask import Flask, jsonify, render_template, request
from app_helper import validate_form
import requests

API_BASE_URL = "http://numbersapi.com"

app = Flask(__name__)

app.config['SECRET_KEY'] = "ABCezas123"

@app.route("/")
def homepage():
    """Show homepage."""
    return render_template("index.html")

@app.route("/api/get-lucky-num", methods=["POST"])
def get_lucky_num():
    """Get lucky number."""
    
    output = validate_form(request.json)
    
    if not bool(output['errors']):
        try:
            response = requests.get(f"{API_BASE_URL}/random?min=1&max=100&json")
            r = response.json()
            output["num"] = {"num": r['number'], "fact": r['text']}
        except:
            output['errors']['lucky_num'] = {"error": "get lucky number failed"}

        try:
            response = requests.get(f"{API_BASE_URL}/{request.json['year']}/year?json")
            r = response.json()
            output["year"] = {"num": r['number'], "fact": r['text']}
        except:
            output['errors']['year'] = "get year failed"

    return jsonify(output)

