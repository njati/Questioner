'''This is the model database for the app'''

class Recordquiz():

    '''Create a questions database'''
    def __init__(self, user_id=0, question='', meetup_id=''):
        self.questions_database = []
        self.question = question
        self.user_id = user_id
        self.meetup_id = meetup_id

    def add_question(self):
        '''Create a new question'''
        new_question_data = {
            "question_id": len(QuestionRecords)+1,
            "meetup_id": self.meetup_id,
            "user_id": self.user_id,
            "question": self.question,
            "votes":0
        }

        self.questions_database.append(new_question_data)
