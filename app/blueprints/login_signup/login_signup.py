from flask import Blueprint, render_template, redirect, request, session
from .models import User
from app.login_required import login_required, logout_required

login_signup_bp = Blueprint("login_signup", __name__, template_folder="templates",static_folder="static")

@login_signup_bp.route("/test")
@login_required
def test():
    return "Logged in"

@login_signup_bp.route("/delete")
@login_required
def delete_account():
    User.delete()
    return redirect('logout')

@login_signup_bp.route("/change_password", methods=["GET","POST"])
@login_required
def change_password():
    if(request.method == 'POST'):
        post = True
        if(not User.check_password()):
            post = False
            error = "Enter the correct current password"
            return render_template('profile/change_password.html',error=error), 400
        if(request.form.get('new_password') != request.form.get('confirm_new_password')):
            post = False
            error = "Confirm password should match the password"
            return render_template('profile/change_password.html',error=error), 400
        if len(request.form.get('new_password')) < 8:
            post = False
            error = "Password should have atleast 8 characters"
            return render_template("signup/signup.html", error = error), 400
        if(post):
            User.change_password()
            return redirect("/user/")

    return render_template('profile/change_password.html')

@login_signup_bp.route("/")
@login_required
def profile():
    return render_template('profile/profile.html',username=session['username'],email=session['email'])

@login_signup_bp.route("/logout")
@login_required
def logout():
    User.logout()
    return redirect("login")


@login_signup_bp.route("/login", methods=["GET", "POST"])
@logout_required
def login():
    if request.method == "GET":
        return  render_template("login/login.html")
    else:
        u = User.check()
        if not u:
            error = "Invalid email or password"
            return  render_template("login/login.html",error=error), 401
        User.login(u)
        return redirect("test")

@login_signup_bp.route("/signup", methods=['GET', "POST"])
@logout_required
def signup():
    if request.method == "GET":
        user_d = {
            "username" : "",
            "email" : "",
        }
        return render_template("signup/signup.html",user_d = user_d)
    else:
        user_d = {}
        user_d["username"] = request.form.get('username')
        user_d["email"] = request.form.get('email')

        post = True
        if len(request.form.get('password')) < 8:
            post = False
            error = "Password should have atleast 8 characters"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
    
        elif request.form.get('password') != request.form.get('confirm_password'):
            post = False
            error = "Confirm password should match the password"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
        
        if User.exists(user_d["email"]):
            post = False
            error = "Email already exists"
            return render_template("signup/signup.html",user_d = user_d, error = error), 400
        if post:
            u = User.signup(user_d["username"], user_d["email"])
            if u:
                User.login(u)
                return redirect("test")
        error = "Sign Up failed. Try again"
        return render_template("signup/signup.html",user_d = user_d, error = error), 500