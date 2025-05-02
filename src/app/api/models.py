## This class acts as Database layer. It had functions to load users, save users used for regiteration and login purposes and load messages, add new messages used by Landing page. Since there is no DB connected data is stored in json files, This functions will pull and push data to the json files
import json
import os


JSON_FILE = '../resources/messages.json'
USERS_FILE= '../resources/users.json'   

 # Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
         return json.load(f)
    return []


def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# Load messages from JSON file
def load_messages():
     if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
     return []

# Save messages to file
def save_messages(messages):
    with open(JSON_FILE, 'w') as f:
        json.dump(messages, f, indent=2)
