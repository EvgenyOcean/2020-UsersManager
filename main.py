from flask import Flask, render_template, request, jsonify, request, redirect, url_for

app = Flask(__name__)

####################
# Main Pages #
####################

# Home page 
@app.route('/')
def home():
    return render_template('home.html')

# User listing page
@app.route('/users')
def users():
    return render_template('list.html')

# User profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')

#####################
# REST APIs #
#####################

# Adding user
@app.route('/api/create', methods=['POST'])
def create_user():
    pass

# Deleting user by an id
@app.route('/api/delete', methods=['DELETE'])
def delete_user():
    pass

# Getting all the users
@app.route('/api/users', methods=['GET'])
def get_users_list():
    pass

# Getting user by an id
@app.route('/api/user', methods=['GET'])
def get_user():
    pass

# Editing user by an id
@app.route('/api/profile', methods=['UPDATE'])
def edit_user():
    pass

