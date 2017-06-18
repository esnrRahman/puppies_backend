from functools import wraps
from flask import g
from flask_login import current_user


def before_request(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        g.user = current_user
        kwargs["user"] = g.user
        r = f(*args, **kwargs)
        return r
    return wrapped
