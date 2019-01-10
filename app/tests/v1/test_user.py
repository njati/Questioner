"""This tests user credentials endpoints"""

import json
import unittest
from app.api import APP

class TestUser(unittest.TestCase):
    
    def setUp(self):

        APP.testing = True

        self.app = APP.test_client()
        self.data = {
            "uname": "user1",
            "email": "email@email.com",
            "password": "password"
        }

    def test_register(self):

        response = self.app.post('/auth/signup',
                                 data = json.dumps(self.data),
                                 content_type="application/json")

        result = json.loads(response.data)

        self.assertEqual(result["status"], "ok")

        self.assertEqual(result["uname"], "user1")
        self.assertEqual(result["email"], "email@email.com")
        
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()

