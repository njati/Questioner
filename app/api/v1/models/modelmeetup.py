'''Model database'''

class MeetupRecords():
    '''Create a meetup database'''
    def __init__(self, meetup_id='', meetup_image='', location='', meetup_date='', topic='', about=''):
        self.meetups_database = []
        self.meetup_id = meetup_id
        self.location = location
        self.meetup_date = meetup_date
        self.topic = topic
        self.about = about
        self.meetup_image = meetup_image

    def add_meetup(self):
        '''Create a new meetup'''
        new_meetup_data = {
            "meetup_id": self.meetup_id,
            "meetup_date": self.meetup_date,
            "topic": self.topic,
            "about":self.about,
            "location":self.location,
            "meetup_image":self.meetup_image
        }

        self.meetups_database.append(new_meetup_data)

    def get_meetup(self, meetup_id):
        for each_meetup in self.meetups_database:
            if each_meetup['meetup_id'] == meetup_id:
                return each_meetup
