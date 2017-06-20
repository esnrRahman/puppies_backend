import os
import traceback

from models import User, Post
from module_helper import ModuleHelper
from db import session
from error_codes import ErrorCodes
from decorators.before_request import before_request

from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_login import login_user, logout_user, login_required
from werkzeug.utils import secure_filename


class TestResource(Resource):
    def get(self):
        status = ErrorCodes.OK

        return make_response(jsonify({"message": "Testing GET API call"}), status)


class SigninResource(Resource):

    # TODO: Need to put a call limiter for APIs that do not have @login_required decorator
    def post(self):
        status = ErrorCodes.INTERNAL_SERVER_ERROR
        message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status], "")

        try:
            json_data = request.get_json(force=True)

            if "email" in json_data and "password" in json_data:
                email = json_data["email"]
                password = json_data["password"]

                user = session.query(User).filter(User.email == email).first()

                if user and user.password == password:
                    login_user(user, remember=True)
                    status = ErrorCodes.OK
                    message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status],
                                                                ErrorCodes.LOG_IN_SUCCESS_MESSAGE)

                    user_dict = ModuleHelper.object_as_dict(user)
                    del user_dict["password"]
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
                del user_dict["password"]
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

    # TODO: Need to put a call limiter for APIs that do not have @login_required decorator
    def post(self):
        status = ErrorCodes.INTERNAL_SERVER_ERROR
        message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status], "")

        try:
            json_data = request.get_json(force=True)

            if "email" in json_data and "password" in json_data:
                email = json_data["email"]
                password = json_data["password"]

                user = session.query(User).filter(User.email == email).first()

                if user:
                    status = ErrorCodes.BAD_REQUEST
                    message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                              ErrorCodes.USER_ALREADY_EXISTS_ERROR_MESSAGE)
                else:
                    new_user = User(email=email,
                                    password=password,
                                    name=json_data["name"] if "name" in json_data else None)

                    session.add(new_user)
                    session.commit()

                    status = ErrorCodes.CREATED
                    message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status], "")

                    new_user_dict = ModuleHelper.object_as_dict(new_user)
                    del new_user_dict["password"]
                    new_user_dict["message"] = message

                    return make_response(jsonify(new_user_dict), status)
            else:
                status = ErrorCodes.BAD_REQUEST
                message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                          ErrorCodes.NO_USERNAME_OR_PASSWORD_ERROR_MESSAGE)

        except Exception as e:
            traceback.print_exc()

        return make_response(jsonify({"message": message}), status)


class PostResource(Resource):
    pass

class UserPostsResource(Resource):
    pass


class PostsResource(Resource):
    @login_required
    @before_request
    def get(self, user=None):
        pass

    @login_required
    @before_request
    def post(self, user=None):
        status = ErrorCodes.INTERNAL_SERVER_ERROR
        message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status], "")

        try:
            filename = None
            content = None
            file = request.files['file']

            if file and ModuleHelper.allowed_file(file.filename):
                filename = secure_filename(file.filename)

                from app import app
                basedir = os.path.abspath(os.path.dirname(__file__))
                file.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))

            # TODO: Not clean but just make it work
            if request.form.getlist("content"):
                content = request.form.getlist("content")

            if filename or content:
                new_post = Post(user_id=user.id,
                                content=content,
                                image_name=filename)

                session.add(new_post)
                session.commit()

                status = ErrorCodes.CREATED
                message = ErrorCodes.SUCCESS_MESSAGE.format(ErrorCodes.responses[status], "")

                new_post_dict = ModuleHelper.object_as_dict(new_post)
                new_post_dict["message"] = message

                return make_response(jsonify(new_post_dict), status)
            else:
                status = ErrorCodes.BAD_REQUEST
                message = ErrorCodes.ERROR_MESSAGE.format(ErrorCodes.responses[status],
                                                          ErrorCodes.POST_NO_CONTENT_OR_IMG_UPLOAD_ERROR_MESSAGE)

        except Exception as e:
            traceback.print_exc()

        return make_response(jsonify({"message": message}), status)


class LikeResource(Resource):
    pass

class LikesResource(Resource):
    pass



