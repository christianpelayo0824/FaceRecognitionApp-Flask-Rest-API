from flask_restful import Resource
from flask import jsonify
from model.User import User


class GetUserByID(Resource):

    def get(self, id):
        users = User()
        data = jsonify(users.get_user_by_id(id))
        data.status_code = 200
        return data
