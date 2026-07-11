#!/usr/bin/python3
"""Simple Flask API for a server for manage data and user"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary (do not include test data)
users = {}


@app.route('/')
def home():
    """Home endpoint it's the main page"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """Data endpoint - returns list of usernames"""
    return jsonify(list(users.keys())), 200


@app.route('/status')
def get_status():
    """Status endpoint, it's the verification of the server"""
    return "OK", 200


@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    try:
        return jsonify(users[username]), 200
    except KeyError:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user"""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    users[data["username"]] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == '__main__':
    app.run()
