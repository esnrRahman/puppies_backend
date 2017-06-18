import traceback

from models import User, Post
from helper import ModuleHelper
from db import session
from error_codes import ErrorCodes
from decorators.before_request import before_request

from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required


class TestResource(Resource):
    def get(self):
        status = ErrorCodes.OK

        return make_response(jsonify({"message": "Testing GET API call"}), status)


class SigninResource(Resource):

    # Need to put a call limiter for APIs that do not have @login_required decorator
    def post(self):
        status = ErrorCodes.INTERNAL_SERVER_ERROR
        message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status], "")

        try:
            json_data = request.get_json(force=True)

            if "username" in json_data and "password" in json_data:
                username = json_data["username"]
                password = json_data["password"]

                # TODO: All db related stuff needs to be moved to module layer
                user = session.query(User).filter(User.username == username, User.password == password).first()

                if user:
                    login_user(user)
                    status = ErrorCodes.OK
                    message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status],
                                                                ErrorCodes.LOG_IN_SUCCESS_MESSAGE)

                    user_dict = ModuleHelper.object_as_dict(user)
                    user_dict["message"] = message

                    return make_response(jsonify(user_dict), status)

                else:
                    status = ErrorCodes.NOT_FOUND
                    message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                              ErrorCodes.USER_NOT_FOUND_ERROR_MESSAGE)
            else:
                status = ErrorCodes.BAD_REQUEST
                message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                          ErrorCodes.NO_USERNAME_OR_PASSWORD_ERROR_MESSAGE)

        except Exception as e:
            traceback.print_exc()

        return make_response(jsonify({"message": message}), status)


class SignoutResource(Resource):
    @login_required
    def get(self):
        status = ErrorCodes.OK
        message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status],
                                                    ErrorCodes.LOG_OUT_SUCCESS_MESSAGE)
        logout_user()

        return make_response(jsonify({"message": message}), status)


class UserResource(Resource):

    @login_required
    @before_request
    def get(self, user_id, user=None):
        status = ErrorCodes.INTERNAL_SERVER_ERROR
        message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status], "")

        try:
            user = session.query(User).filter(User.id == user_id).first()

            if user:
                status = ErrorCodes.OK
                message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status],
                                                            ErrorCodes.FOUND_USER_SUCCESS_MESSAGE)

                user_dict = ModuleHelper.object_as_dict(user)
                user_dict["message"] = message

                return make_response(jsonify(user_dict), status)

            else:
                status = ErrorCodes.NOT_FOUND
                message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                          ErrorCodes.USER_NOT_FOUND_ERROR_MESSAGE)

        except Exception as e:
            traceback.print_exc()

        return make_response(jsonify({"message": message}), status)

class CreateUserResource(Resource):
    pass

class PostResource(Resource):
    pass

class UserPostsResource(Resource):
    pass

class PostsResource(Resource):
    pass

class LikeResource(Resource):
    pass

class LikesResource(Resource):
    pass

