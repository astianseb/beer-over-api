#!/bin/python

#feature-001

from flask import Flask, jsonify, request, render_template
import uuid
import random

# Initialize the Flask application
app = Flask(__name__)


# This route will return a list in JSON format
@app.route('/')
def index():
    return render_template('index.html')
    


@app.route('/brewme')
def clone():
    given_number = int(request.query_string)
    uuid_list = []
    beer_type_list = ["ale", "brown-ale", "IPA", "AIPA", "lager", "wheat"]
    for i in range(given_number):
        uuid_list.append({"beer_number": i, "beer_type": random.choice(beer_type_list), "beer_ID": uuid.uuid4()})
    return jsonify(beer_batch=uuid_list)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )

