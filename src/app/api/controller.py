from flask import Flask, request, jsonify
from flask_cors import CORS
from service import create_new_message, get_all_messages, login_user, register_user

app = Flask(__name__)
CORS(app)  # Allow CORS for all origins (for development)


# Rest Api endpoint for Registeration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result= register_user(data)
    return result

# Rest Api endpoint for Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result =login_user(data)
    return result

# Rest API to add a message and save to file
@app.route('/addMessage', methods=['POST'])
def add_message():
    result = create_new_message(request)
    return result

# Rest API to GET route to retrieve messages
@app.route('/getMessages', methods=['GET'])
def get_messages():
   result = get_all_messages(request)
   return result



if __name__ == '__main__':
    app.run(debug=True)
