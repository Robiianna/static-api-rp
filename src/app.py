"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson", [{
            "first_name": "John",
            "last_name": "Jackson",
            "age": 33,
            "lucky_numbers":[7,13,22]
        },
        {
            "first_name": "Jane",
            "last_name": "Jackson",
            "age": 35,
            "lucky_numbers":[10,14,3]
        },
        {
            "first_name": "Jimmy",
            "last_name": "Jackson",
            "age": 5,
            "lucky_numbers":[1]
}])

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    # members = json.loads(request.data)
    return jsonify(members),200


@app.route('/member', methods=['POST'])
def add():
    id = request.json.get("id")
    first_name = request.json.get("first_name")
    age = request.json.get("age")
    lucky_numbers = request.json.get("lucky_numbers")
    new_member = {
        "id": id,
        "first_name": first_name,
        "last_name": "Jackson",
        "age": age,
        "lucky_numbers": lucky_numbers 
    }
    jackson_family.add_member(new_member)
    return jsonify(first_name),200

@app.route('/member/<int:member_id>', methods=['GET', 'DELETE'])
def get_jackson(member_id):
    if request.method == "GET":
        member = jackson_family.get_member(member_id)
        return jsonify(member),200
    else:
        member = jackson_family.delete_member(member_id)
        return jsonify({
            "done": True
        }),200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
#this

