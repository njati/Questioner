'''Model database'''

class Records():
    '''Create a meetup database'''
    def __init__(self, meetup_image='', location='', meetup_date='', topic='', about=''):
        self.meetups_database = []
        self.location = location
        self.meetup_date = meetup_date
        self.topic = topic
        self.about = about
        self.meetup_image = meetup_image

    def add_meetup(self):
        '''Create a new meetup'''
        new_meetup_data = {
            "meetup_date": self.meetup_date,
            "topic": self.topic,
            "about": self.about,
            "location": self.location,
            "meetup_image":self.meetup_image
        }

        self.meetups_database.append(new_meetup_data)
