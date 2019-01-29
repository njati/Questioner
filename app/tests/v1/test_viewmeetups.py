"""This tests meetup credentials endpoints"""

import json
import unittest
from app.api import APP

class Testmeetup():
    def setUp(self):

        APP.testing = True

        self.app = APP.test_client()

    def test_createmeetup(self):

        data = {
            "meetup_date":"2019-08-09",
            "topic":"Hello world",
            "about":"About",
            "location": "Nairobi",
            "meetup_image":"Hello"
        }
        response = self.app.post('/meetups',
                                 data=json.dumps(data),
                                 content_type="application/json")

        result = json.loads(response.data)

        self.assertEqual(result["meetup_date"], "2019-08-09")

        self.assertEqual(result["topic"], "Hello world")
        self.assertEqual(result["about"], "About")
        self.assertEqual(result["location"], "Nairobi")
        self.assertEqual(result["meetup_image"], "Hello")

        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()
