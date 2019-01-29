
from flask import Blueprint, request, jsonify, abort,make_response
from app.api.v1.models.modelupdown import CounterDownvotes, CounterUpvotes
from app.api.v1.views.viewquestions import Recordquiz

VOTES_BLUEPRINT = Blueprint('Votes_here', __name__)



@VOTES_BLUEPRINT.route('/questions/upvote',methods=['PATCH'])
def upvotes():
    data = request.get_json()
    Quizn = CounterUpvotes(data['question_id'])
    Quizn = CounterUpvotes.add_upvote(Quizn)

    if Quizn == None:
        return make_response("Not found", 404)
    else:
        return make_response(Quizn,201)

@VOTES_BLUEPRINT.route('/questions/downvote',methods=['PATCH'])
def downvote():
    data = request.get_json()
    Quizn = CounterDownvotes(data['question_id'])
    Quizn = CounterDownvotes.new_downvote(Quizn)

    if Quizn == None:
        return make_response("Not found", 404)
    else:
        return make_response(Quizn,201)








