import base64
import requests
from flask import Flask, jsonify, request
import json

# declared an empty variable for reassignment
response = []
count = 0

# creating the instance of our flask application
app = Flask(__name__)

# route to entertain our post and get request from flutter app
@app.route('/name', methods=['GET', 'POST'])
def nameRoute():

    # fetching the global response variable to manipulate inside the function
    global response
    global count

    # checking the request type we get from the app
    if(request.method == 'POST'):
        file = request.files['name']
        images = [base64.b64encode(file.read()).decode("ascii")]
        your_api_key = "y9wOjqSB8ORZ2O4bPfyk3oYlgl8PIo8PpLaMOoadhwMrhGQtkP"
        json_data = {
            "images": images,
            "modifiers": ["similar_images"],
            "plant_details": ["common_names", "url", "wiki_description", "taxonomy"]
        }
        res = requests.post(
            "https://api.plant.id/v2/identify",
            json=json_data,
            headers={
                "Content-Type": "application/json",
                "Api-Key": your_api_key
            }).json()
        for suggestion in res["suggestions"]:
            response.append(suggestion["plant_name"])
            count = count + 1
        return " "  # to avoid a type error

    else:
        try1 = len(response)
        try2 = try1 - count
        count = 0
        # sending data back to your frontend app
        return jsonify({'name': response[try2]})

if __name__ == "__main__":
    app.run(port="8000", host='127.0.0.1', debug=True)
