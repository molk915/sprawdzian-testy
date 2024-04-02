from flask import Blueprint, request, jsonify
from .logic import UserManager

users_blueprint = Blueprint('users', __name__)
user_manager = UserManager()

@users_blueprint.route('/users', methods=['GET'])
def get_users():
    users = user_manager.get_all_users()
    users_dict = [user.to_dict() for user in users]
    return jsonify(users_dict), 200

@users_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_manager.get_user(id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return "User not found", 404

@users_blueprint.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = user_manager.add_user(**data)
    return jsonify(user.to_dict()), 201

@users_blueprint.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    data = request.json
    user = user_manager.update_user(id, **data)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return "User not found", 404

@users_blueprint.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = user_manager.delete_user(id)
    if user:
        return "User deleted", 200
    else:
        return "User not found", 404
