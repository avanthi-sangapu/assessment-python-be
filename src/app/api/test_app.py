import unittest
from unittest.mock import patch
from controller import app

class FlaskApiTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    @patch('controller.register_user')  # Patch where it's used, not defined
    def test_register_post(self, mock_register_user):
        # Mock the response from the register_user function
        mock_register_user.return_value = {
            "message": "User registered successfully",
            "username": "testuser"
        }
        payload = {
            "username": "testuser",
            "email": "testemail",
            "role": "testrole",
            "password": "testpassword",
        }
        response = self.client.post('/register',json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_register_user.return_value)

    def test_register_post_missing_fields(self):
        # Mock the response from the register_user function
        payload = {
            "email": "testemail",
            "role": "testrole",
            "password": "testpassword",
        }
        response = self.client.post('/register', json=payload)

        self.assertEqual(response.status_code, 400)

    @patch('controller.login_user')
    def test_login_post(self, mock_login_user):
        # Mock the response from the login_user function
        mock_login_user.return_value = {
        "message": 'Login successful',
        "user_id": 1,
        "username": "testuser",
        "role": "testrole",
        'token': '0vdhfdfdfjejfjfj',
        
        }
        
        payload = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post('/login',json=payload)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json,  mock_login_user.return_value)

    def test_login_post_invalid_user(self):
        payload = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post('/login', json=payload)

        self.assertEqual(response.status_code, 401)


    @patch('controller.create_new_message')
    def test_add_message(self, mock_create_new_message):
        # Mock the response from the login_user function
        mock_create_new_message.return_value = {'message': 'Message added', 'data': "Hi how are you"}
        payload = {
            "id": 1,
            "userId": 100,
            "text": "test text"
        }
        response = self.client.post('/addMessage',json=payload)

        self.assertEqual(response.status_code, 200)

    def test_add_message_invalid_authorization(self):
        payload = {
            "id": 1,
            "userId": 100,
            "text": "test text"
        }
        response = self.client.post('/addMessage',json=payload)

        self.assertEqual(response.status_code, 401)

    @patch('controller.get_all_messages')
    def test_get_messages(self, mock_get_messages):
        # Mock the response from the login_user function
        mock_get_messages.return_value = [{
            "id": 1,
            "userId": 100,
            "text": "Hi from Avanthi"
            },
        ]

        response = self.client.get('/getMessages')

        self.assertEqual(response.status_code, 200)


    def test_get_messages_invalid_authorization(self):
        response = self.client.get('/getMessages')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
