from flask import request, jsonify
from flask_restful import Resource
from app.services import UserService

class UserList(Resource):
    def get(self):
        return jsonify(UserService.get_all_users())

    def post(self):
        data = request.get_json()
        return UserService.create_user(data)

class UserDetail(Resource):
    def get(self, user_id):
        user = UserService.get_user_by_id(user_id)
        if not user:
            return {"error": "User not found"}, 404
        return jsonify(user)

    def put(self, user_id):
        data = request.get_json()
        return UserService.update_user(user_id, data)

    def delete(self, user_id):
        return UserService.delete_user(user_id)

def initialize_routes(api):
    api.add_resource(UserList, "/users")
    api.add_resource(UserDetail, "/users/<user_id>")
