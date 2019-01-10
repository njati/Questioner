"""This is the module with all endpoint-routes"""
 
from flask import Blueprint, request, jsonify, make_response

USERVIEW = Blueprint('USERVIEW', __name__)
   
    
@USERVIEW.route('/signin', methods=['POST'])
def login():

    data = request.get_json()
    uname = data['uname']
    email = data['email']

    return make_response(jsonify({
        "status": "ok",
        "uname": uname,
        "email": email
    }), 201)
