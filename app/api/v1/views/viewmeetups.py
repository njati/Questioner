'''Create post new meetup endpoint'''
import datetime
from flask import Blueprint, request, jsonify, make_response
from operator import itemgetter
from app.api.v1.models.modelmeetup import MeetupRecords

MEETUP = Blueprint('create_a_meetup', __name__)

MEETUP_DETAILS = MeetupRecords()


@MEETUP.route('/meetups', methods=['POST'])
def meetups():
    '''fresh meetup endpoint'''
    data = request.get_json()
    meetup_data = {
        "meetup_id": len(MEETUP_DETAILS.meetups_database)+1,
        "created_at":datetime.datetime.now(),
        "meetup_date":data["meetup_date"],
        "topic":data["topic"],
        "about":data["about"],
        "location":data["location"],
        "meetup_image":data["meetup_image"]

    }

    MEETUP_DETAILS.meetups_database.append(meetup_data)
    return make_response(jsonify(meetups_data), 201)


@MEETUP.route('/meetups/<int:id>', methods=['GET'])
def specific_meetups(id):
    new_meetup = MeetupRecords.get_meetup(MEETUP_DETAILS, id) 
    return make_response(jsonify({"data":new_meetup}),200)


@MEETUP.route('/meetups', methods=['GET'])
def allmeetups():
    results = sorted(MEETUP_DETAILS.meetups_database , key=itemgetter('created_at'), reverse=True)
    return make_response(jsonify(results), 201)
