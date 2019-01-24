
from app.api.v1.models.modelquestions import Recordquiz

Recordquestions = Recordquiz()

class CounterUpvotes():

    def __init__(self, user_id, vote_id): 
        self.upvotes_database = []

    def add_upvote(self, user_id, vote_id):
        new_upvote = {
            "voteid": self.vote_id,
            "userid":self.user_id
        }

        for vote in self.upvotes_database:
            if vote["user_id"] == self.user 
                self.upvotes_database.remove(new_upvote)
            else:
                self.upvotes_database.append(new_upvote)

         

class CounterDownvotes():

    def __init__(self, downvote = ''): 
        self.downvotes_database = []
        
      def new_downvote(self):
        new_downvote =
        {
            "user": self.user
            "userid":self.id
        }

         for vote in self.downvotes_database:
            if vote["user"] == self.user 
                self.downvotes_database.remove(new_downvote)
            else:
                self.downvotes_database.append(new_downvote)