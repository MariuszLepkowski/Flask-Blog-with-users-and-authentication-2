from flask import abort
from functools import wraps
from flask_login import current_user


def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous or current_user.id != 1:
            abort(403)
        else:
            return func(*args, **kwargs)
    return decorated_function
