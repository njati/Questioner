'''This is the model database for the app'''

class Recordquiz():
    questions_database = []
    '''Create a questions database'''
    def __init__(self, user_id=0, question='', meetup_id=''):
        self.question = question
        self.user_id = user_id
        self.meetup_id = meetup_id

    def add_question(self):
        '''Create a new question'''
        new_question_data = {
            "question_id": len(QuestionRecords)+1,
            "meetup_id": self.meetup_id,
            "user_id":self.user_id,
            "question":self.question,
            "upvotes":0,
            "downvotes":0
        }

        self.questions_database.append(new_question_data)

    def upvote(self, question_id):
        '''Increment votes'''
        for question in self.questions_database:
            if question['question_id'] == question_id:
                question['upvotes'] += 1
                return question

    def undoupvote(self, question_id):
        '''Increment votes'''
        for question in self.questions_database:
            if question['question_id'] == question_id:
                question['upvotes'] -= 1
                return question

        

    def downvote(self, question_id):
        '''Decrement votes'''
        for question in self.questions_database:
            if question['question_id'] == question_id:
                question['downvotes'] += 1
                return question

    def undodownvote(self, question_id):
        '''Decrement votes'''
        for question in self.questions_database:
            if question['question_id'] == question_id:
                question['downvotes'] -= 1
                return question
