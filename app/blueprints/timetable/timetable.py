from flask import Blueprint, render_template, redirect

timetable_bp = Blueprint("timetable", __name__, template_folder="templates",static_folder="static")

@timetable_bp.route("/")
def timetable():
    return "TimeTable Page"