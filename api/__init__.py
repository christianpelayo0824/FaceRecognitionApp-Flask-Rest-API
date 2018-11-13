from flask_restful import Api

from app import appInstance
from .GetAllUser import GetAllUser
from .GetUserByID import GetUserByID
from .DeleteUserByID import DeleteUserByID

restServer = Api(appInstance)

restServer.add_resource(GetAllUser, '/api/getAllUser')
restServer.add_resource(GetUserByID, '/api/getUserById/<int:id>')
restServer.add_resource(DeleteUserByID, '/api/deleteUserById/<int:id>')