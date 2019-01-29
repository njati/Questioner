
from flask import jsonify
from app.api.v1.models.modelquestions import Recordquiz

Recordquestions = Recordquiz()

class CounterUpvotes():
    upvotes_database = []

    def __init__(self,question_id): 
        self.userId = 1  #user_id for user making request
        self.questionId = question_id


    def add_upvote(self):
        new_upvote = {
            "questionid":self.questionId,
            "userid":self.userId
        }

        if new_upvote in self.upvotes_database:
            self.upvotes_database.remove(new_upvote)
            record = Recordquestions.undoupvote(self.questionId)
        else:
            self.upvotes_database.append(new_upvote)
            record = Recordquestions.upvote(self.questionId)

        return jsonify(record)

         
class CounterDownvotes():
    downvotes_database = []

    def __init__(self, question_id): 
        self.user = 1 #user id of user making request
        self.questionId = question_id

        
    def new_downvote(self):
        new_downvote = {
            "userid": self.user,
            "questionid":self.questionId
        }

        if new_downvote in self.downvotes_database:
            self.downvotes_database.remove(new_downvote)
            record = Recordquestions.undodownvote(self.questionId)
        else:
            self.downvotes_database.append(new_downvote)
            record = Recordquestions.downvote(self.questionId)

        return jsonify(record)