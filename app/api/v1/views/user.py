"""This is the module with all endpoint-routes"""
 
from flask import Blueprint, request, jsonify, make_response

USERVIEW = Blueprint('USERVIEW', __name__)
   
    
@USERVIEW.route('/login', methods=['POST'])
def login():

    data = request.get_json()
    username = data['uname']
    email = data['email']

    return make_response(jsonify({
        "status": "ok",
        "username": username,
        "email": email
    }), 201)
