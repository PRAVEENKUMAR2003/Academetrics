from flask import Blueprint, render_template, redirect

courses_bp = Blueprint("courses", __name__, template_folder="templates",static_folder="static")

@courses_bp.route("/")
def courses():
    return "Courses Page"