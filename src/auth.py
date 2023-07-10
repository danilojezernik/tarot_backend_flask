from src.domain.user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    user = User(user=username, geslo=password, tip='ADMIN')  # Replace None with the appropriate user type
    if user and safe_str_cmp(user.geslo.encode('utf-8'), password.encode('utf-8')):
        return user


def identity(payload):
    user_id = payload['identity']
    # Retrieve the user based on the user_id from the payload
    return user_id
