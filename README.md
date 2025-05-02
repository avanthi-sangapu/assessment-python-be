# assessment-python-be

## Description
This project is used as backend service which serves Rest Web services using Python Flask framework. We have different web services for Registeration, Login, Showing Messages and Adding new messages. Since it is local project withou database setup, this project contains json files for storing User and Messages. We also have some methods to load this json to python code, so that it can be used as data in above functionalities.


## Getting Started
This is a Python implementation of Python Flask.
List any dependencies that need to be installed, such as:

- Python 3.13.3
- Flask 3.1.0
  Flask-cors 5.0.1
  bcrypt 4.3.0
  PyJWT 2.10.1


## Project Structure
The code is inside src/app folder. api folder will have python code for REST APIs and their test cases, resources folder will have 2 json files to hold data of users and messages used in Landing page. 
controller.py - main controller which has API endpointf for Registeration, Login, Get Messages and Add new Message
service.py- acts a service layer where it gets request from controller and does the business logic connecting to models which holds data
models.py- acts as database layer which has functions to load data from json file
test_app.py- has unit test cases


### Installation

Steps to install the application:

```shell
git clone https://github.com/avanthi-sangapu/assessment-python-be.git
cd <project-directory>
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
1. Install Python 3.13.3 from https://www.python.org/downloads/
2. Run pip install Flask,pip install flask-cors,pip install bcrypt, pip install PyJWT
3. 

### Run Application
1. Change directory to src/app/api and run command python controller.py on terminal of VS Studio or command prompt
2. Test the login, register, messages, add_messages API calls from tool like Insomnia
3. Thr url for register api is http://127.0.0.1:5000/register and it is post request and body is

    {
  "username": "testusername",
  "email": "testemail@gmail.com",
  "role": "testrole",
  "password": "testpassword"
   }
4. Thr url for login api is http://127.0.0.1:5000/login and it is post request and body is

    {
  "username": "testusername",
  "password": "testpassword"
   }

5. The url for getting Messages is http://127.0.0.1:5000/getMessages, request is get and expects response as
[
  {
    "id": 1,
    "text": "Hello from Alice!",
    "userId": 101
  },
  {
    "id": 2,
    "text": "Hi from Bob!",
    "userId": 102
  }
]

6. The url for adding new messages is  http://127.0.0.1:5000/addMessages, request is post, body is
    {
  "id": 0,
  "userId": 113,
  "text": "Hi"
}

7. load_users method is used for loading users form Users.json file
8. save_users method is used for saving or updating users to Users.json file
9. load_messages method is used for loading messages form Messages.json file
10. save_messages method is used for saving or updating messages to Messages.json file
11. Bcrypt is used for securly hashing and verifying passwords.
12. PyJWT library is used for generating JWT token when user logins and verifies the token when user hits any service after login
