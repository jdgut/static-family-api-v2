"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User
#from models import Person
from datastructures import FamilyStructure
# from classes import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

# jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route("/members")
def create_family_tree():
    grandParent = FamilyStructure("Jackson", "Joe", 50)
    firstParent = FamilyStructure("Jackson", "Michael", 30)
    secondParent = FamilyStructure("Jackson", "Randy", 35)

    fcFP = FamilyStructure("Jackson", "Paris", 18)
    scFP = FamilyStructure("Jackson", "Blanket", 17)

    fcSP = FamilyStructure("Jackson", "Steven", 13)
    scSP = FamilyStructure("Jackson", "Stevana", 21)

    firstParent.addChild(fcFP.getData())
    firstParent.addChild(scFP.getData())

    secondParent.addChild(fcSP.getData())
    secondParent.addChild(scSP.getData())
    
    grandParent.addChild(firstParent.getData())
    grandParent.addChild(secondParent.getData())

    return jsonify(grandParent.getData()), 200


# @app.route("/members/setup")
# def create_family_tree():
#     grandParent = FamilyStructure("Joe", "Jackson", 50)
#     parentOne = FamilyStructure("Michael", "Jackson", 30)
#     parentTwo = FamilyStructure("Ray", "Jackson", 40)
#     pOneChildOne = FamilyStructure("Paris", "Jackson", 25)
#     parentOne.addChild(pOneChildOne)
#     return jsonify(parentOne.getData()), 200

# @app.route('/members')
# def create_family_tree():
#     members = jackson_family.getAllMembers()
#     grandparent = members[0]
#     first_parent = jackson_family.createFamilyMember("Michael", 40, grandparent['id'])
#     second_parent = jackson_family.createFamilyMember("Randy", 45, grandparent['id'])
#     fp_fc = jackson_family.createFamilyMember("Paris", 18, first_parent['id'])
#     fp_sc = jackson_family.createFamilyMember("Prince", 17, first_parent['id'])
#     sp_fc = jackson_family.createFamilyMember("Stevana", 28, second_parent['id'])
#     sp_sc = jackson_family.createFamilyMember("Steve", 21, second_parent['id'])

#     family_tree = jackson_family.getAllMembers()
#     return jsonify(family_tree), 200

# @app.route('/members/all')
# def get_members():
#     family_tree = []
#     pos_id = []
#     for idx, member in enumerate(jackson_family.getAllMembers()):
#         if 'children' in member.keys() and len(member['children']) > 0:
#             children = jackson_family.getChildren(member["id"])
#             family = {
#                 'id'        :   member['id'],
#                 'first_name':   member['first_name'],
#                 'last_name' :   member['last_name'],
#                 'age'       :   member['age'],
#                 'children'  :   children  
#             }
#             family_tree.append(family)

#     return jsonify(family_tree), 200

# @app.route('/member/<int:id>')
# def get_single_member(id):
#     member = jackson_family.getSingleMember( int(id) )
#     if member is None:
#         return jsonify("Not found"), 404
#     else:
#         return jsonify(member), 200

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
