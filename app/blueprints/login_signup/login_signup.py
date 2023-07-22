from flask import Blueprint, render_template, redirect, request
from .models import User
from app.login_required import login_required

login_signup_bp = Blueprint("login_signup", __name__, template_folder="templates",static_folder="static")

@login_signup_bp.route("/test")
@login_required
def test():
    return "Logged in"

@login_signup_bp.route("/logout")
def logout():
    User().logout()
    return  redirect("login")

@login_signup_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return  render_template("login/login.html")
    else:
        user = User()
        u = user.check()
        if not u:
            error = "Invalid email or password"
            return  render_template("login/login.html",error=error), 401
        user.login(u)
        return redirect("test")

@login_signup_bp.route("/signup", methods=['GET', "POST"])
def signup():
    if request.method == "GET":
        user_d = {
            "username" : "",
            "email" : "",
            "password" : "",
            "confirm_password" : ""
        }
        return render_template("signup/signup.html",user_d = user_d)
    else:
        user_d = {}
        user_d["username"] = request.form.get('username')
        user_d["email"] = request.form.get('email')
        user_d["password"] = request.form.get('password')
        user_d["confirm_password"] = request.form.get('confirm_password')
        post = True
        if len(user_d["password"]) < 8:
            post = False
            error = "Password should have atleast 8 characters"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
    
        elif user_d["password"] != user_d["confirm_password"]:
            post = False
            error = "Confirm password should match the password"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
        user = User()
        if user.exists():
            post = False
            error = "Email already exists"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
        if post:
            u = user.signup()
            if u:
                user.login(u)
                return redirect("test")
        error = "Sign Up failed. Try again"
        return render_template("signup/signup.html",user_d = user_d, error = error), 500