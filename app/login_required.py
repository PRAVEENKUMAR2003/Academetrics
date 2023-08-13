from functools import wraps
from flask import session, redirect
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/user/login")
    return wrap

def logout_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" not in session:
            return f(*args, **kwargs)
        else:
            return redirect("/user/test")
    return wrap