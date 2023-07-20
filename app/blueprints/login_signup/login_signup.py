from flask import Blueprint, render_template, redirect

login_signup_bp = Blueprint("login_signup", __name__, template_folder="templates",static_folder="static")

@login_signup_bp.route("/login")
def login():
    return "Login Page"