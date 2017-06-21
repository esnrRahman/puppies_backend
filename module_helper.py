import json
import re
from sqlalchemy import inspect

class ModuleHelper(object):

    # @classmethod
    # def check_email_syntax(cls, input_email):
    #     """
    #     Check for correct email syntax
    #     :param input_email:
    #     :return:
    #     """
    #     email_regex = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    #
    #     if not re.match(email_regex, input_email):
    #         return False
    #
    #     return True

    @classmethod
    def object_as_dict(cls, obj):
        """
        Convert an SqlAlchemy object to a dict
        :param obj: 
        :param message: 
        :return: 
        """
        return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

    @classmethod
    def allowed_file(cls, filename):
        from app import app
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
