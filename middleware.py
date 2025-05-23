from functools import wraps
from flask import session, redirect

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("email"):
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function
