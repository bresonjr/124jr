
from flask import Flask,jsonify, request
app = Flask(__name__)
List = [
    {
        'id': 1,
        'Name': u'BRESON',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'NARUTO',
        'Contact': u'9876543222', 
        'done': False
    }
]
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)
    contact = {
        'id': add_task[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 
if (__name__ == "__main__"):
    app.run(debug=True)
    