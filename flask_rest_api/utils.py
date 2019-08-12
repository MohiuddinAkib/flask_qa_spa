from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user = get_jwt_identity()
        result = f(*args, **kwargs)
        print(current_user)
        if not current_user.get('admin'):
            result = jsonify({'msg': 'Unauthorized'}), 403
        return result

    return decorated_function
