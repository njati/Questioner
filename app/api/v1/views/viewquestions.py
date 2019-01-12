'''Create post new question endpoint'''
import datetime
from flask import Blueprint, request, jsonify
from app.api.v1.models.modelquestions import Recordquiz

QUESTION_BLUEPRINT = Blueprint('add_a_question', __name__)

QUESTION_DETAILS = Recordquiz()


@QUESTION_BLUEPRINT.route('/questions', methods=['POST'])
def post_question():
    '''Create user new question endpoint'''
    data = request.get_json()

    question = data["question"]
    title = data["title"]
    meetup_id = data["meetup_id"]
    user_id = data["user_id"]

    questions_data = {
        "question_id": len(QUESTION_DETAILS.questions_database)+1,
        "created_at": datetime.datetime.now(),
        "question": question,
        "title": title,
        "meetup_id":meetup_id,
        "user_id":user_id

    }

    QUESTION_DETAILS.questions_database.append(questions_data)
    return jsonify(QUESTION_DETAILS.questions_database), 201
