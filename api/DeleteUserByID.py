from flask_restful import Resource
from flask import jsonify
from model.User import User


class DeleteUserByID(Resource):

    def delete(self, id):
        users = User()
        data = users.delete_user(id)
        data.status_code = 200
        return data
