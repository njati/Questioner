'''Create post new meetup endpoint'''
import datetime
from flask import Blueprint, request, jsonify
from app.api.v1.models.modelmeetup import Records

MEETUP = Blueprint('create_a_meetup', __name__)

MEETUP_DETAILS = MeetupRecords()


@MEETUP.route('/meetups', methods=['POST'])
def meetups():
    '''fresh meetup endpoint'''
    data = request.get_json()
    meetup_date = data["meetup_date"]
    topic = data["topic"]
    about = data["about"]
    location = data["location"]
    meetup_image = data["meetup_image"]

    meetup_data = {
        "meetup_id": len(MEETUP_DETAILS.meetups_database)+1,
        "created_at": datetime.datetime.now(),
        "meetup_date": meetup_date,
        "topic": topic,
        "about": about,
        "location": location,
        "meetup_image":meetup_image

    }

    MEETUP_DETAILS.meetups_database.append(meetup_data)
    return jsonify(MEETUP_DETAILS.meetups_database), 201
