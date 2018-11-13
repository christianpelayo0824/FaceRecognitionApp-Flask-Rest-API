from flask_restful import Resource
from flask import jsonify
from model.User import User


class GetAllUser(Resource):

    def get(self):
        users = User()
        data = jsonify(users.get_all_user())
        data.status_code = 200
        return data
