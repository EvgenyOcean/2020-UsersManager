import os
from flask import Flask, render_template, request, jsonify
from models import UserHandler

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

####################
# Main Pages #
####################

# Home page 
@app.route('/')
def home():
    return render_template('home.html')

# User profile page
@app.route('/profile/')
def profile():
    return render_template('profile.html')

####################
# Utils #
####################

def user_data_validators(data, username):
    first_name = data.get('firstName', '')
    last_name = data.get('lastName', '')

    # small validation section
    if len(username) > 16 or len(username) < 4:
        return "Username must be 4-16 characters long"
    if len(first_name) > 16:
        return "First name must be 4-16 characters long"
    if len(last_name) > 16:
        return "Last name must be 4-16 characters long"

    new_user = {
        'username': username, 
        'first_name': first_name,
        'last_name': last_name,
    }

    return new_user

#####################
# REST APIs #
#####################

# Adding user
@app.route('/api/create/', methods=['POST'])
def create_user():
    if request.is_json:
        data = request.get_json()
        try:
            username = data['username']
        except KeyError:
            return jsonify({"message": "Username is required"}) 

        validation_result = user_data_validators(data, username)
        if type(validation_result) == str:
            return jsonify({"message": validation_result})

        # so basically, what these two lines of code do: 
        # 1. init db, using specified path, by default db is expected to be in the root folder
        # 2. call specific method, depending on the operation to be performed
        database = UserHandler()
        result = database.add_user(validation_result)
        
        return jsonify({"message": result})

    else:
        return jsonify({"message": "Wrong content-type"})

# Getting all the users
@app.route('/api/users/', methods=['GET'])
def get_users_list():
    database = UserHandler()
    users = database.get_users()
    return jsonify(users)

# Deleting user by an id
@app.route('/api/delete/', methods=['DELETE'])
def delete_user():
    if request.is_json:
        try:
            user_id = int(request.get_json()['id'])
        except (KeyError, ValueError): 
            return jsonify({"message": "numeric ID is required"})
        
        database = UserHandler()
        result = database.delete_user(user_id)

        return jsonify({"message": result})

    else:
        return jsonify({"message": "Wrong content-type"})

# Getting user by an id
@app.route('/api/user/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    database = UserHandler()
    result = database.get_user(user_id)
    return jsonify(result) if type(result) == dict else jsonify({"message": result})

# Editing user by an id
@app.route('/api/profile/', methods=['PUT'])
def edit_user():
    if request.is_json:
        data = request.get_json()
        try:
            username = data['username']
            user_id = int(data['id'])
        except (KeyError, ValueError): 
            return jsonify({"message": "numeric ID and username are required"})

        validation_result = user_data_validators(data, username)
        if type(validation_result) == str:
            return jsonify({"message": validation_result})

        validation_result.update({'id': user_id})
        
        database = UserHandler()
        result = database.update_user(user_id, validation_result)
        
        return jsonify({"message": result})

    else:
        return jsonify({"message": "Wrong content-type"})