
from flask import Blueprint, request, jsonify, abort,make_response
from app.api.v1.models.modelupdown import CounterDownvotes, CounterUpvotes

VOTES_BLUEPRINT = Blueprint('Votes_here', __name__)

UPVOTES = CounterUpvotes()
DOWNVOTES_DETAILS = CounterDownvotes()


@VOTES_BLUEPRINT.route('/questions/<int:id>/upvote',methods=['PATCH'])
@VOTES_BLUEPRINT.route('/questions/<int:id>/downvote',methods=['PATCH'])
def votes(id):
    if request.endpoint == 'apiv1.upvote':
        Quizn = quiz().upvotes(id,user=1)
        abort(make_response(jsonify({"data":Quizn}),201))
    elif request.endpoint == 'apiv1.downvote':
        Quizn = quiz().downvotes(id,user=1)
        abort(make_response(jsonify({"data":Quizn}),201)) 








