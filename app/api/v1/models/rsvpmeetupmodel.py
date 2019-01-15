#This is the rsvp model


class rsvpmeetups:

    def __init__(self, meetupid, userid, statustype):
        self.allrsvps = []
        self.meetup_id = meetupid
        self.user_id = userid
        self.statustype = statustype
    
    def creatersvp(self):

        createdrsvps =  {
            "meetup_id": self.meetup_id,
            "user_id": self.user_id,
            "statustype": self.statustype
        }

        self.allrsvps.append(createdrsvps)
        return self.allrsvps




             




