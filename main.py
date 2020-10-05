from flask import Flask, render_template, request, jsonify, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return jsonify({'message': 'Hello World!'})