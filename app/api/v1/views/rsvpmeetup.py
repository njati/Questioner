"""Meetup Views Module"""
# Third Party Imports.
import json
from flask import Response, request, Blueprint, make_response, jsonify
from app.api.v1.models.rsvpmeetupmodel import rsvpmeetups

RSVP_API = Blueprint('rsvp meetup', __name__)

# Local Imports
from app.api.v1.models.rsvpmeetupmodel import rsvpmeetups

@RSVP_API.route('/rsvp', methods=["POST"])  
def rsvpmeet():

        """Creating an RSVP to an event."""
        request_data = request.get_json()
        meetup_id = request_data["meetupid"]
        user_id = request_data["userid"]
        response = request_data["type"]
            
        created_rsvp = rsvpmeetups(meetup_id, user_id, response)
         
        rsvp = created_rsvp.creatersvp()

        response_payload = {
            "status": 201,
            "data": rsvp
        }
        
        response = Response(json.dumps(response_payload), status=201, mimetype="application/json")
        return response 



        


