from flask import Flask
from flask import request
import json

app = Flask(__name__)

users = [];
id = 1;

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!\n", 200

@app.route('/users', methods=['POST'])
def new_users():
    global id, users
    name = request.form["name"]
    name_object = {"id":id,"name":name}
    id= id+1
    users.append(name_object)
    return json.dumps(name_object, indent=4) + "\n", 201

@app.route('/users/<int:id>', methods=['GET'])
def get_users(id):
    name_object = next((user for user in users if user["id"] == id), False)
    if(name_object):
        return json.dumps(name_object, indent=4) + "\n", 200
    # if id doesn't exist return 404
    return "\n", 404

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_users(id):
    users[:] = [user for user in users if user.get('id') != id]
    return "\n", 204
