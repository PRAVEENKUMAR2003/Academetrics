from flask import Blueprint, render_template, redirect, request
from .models import Course
courses_bp = Blueprint("courses", __name__, template_folder="templates",static_folder="static")
from app.login_required import login_required


@courses_bp.route("/")
@login_required
def courses():
    list = Course().course_list()
    return render_template("courses/courses.html", list = list)

@courses_bp.route("/go_course/<id>")
@login_required
def go_course(id):
    course = Course().course_details(id)
    return render_template("courses/course_page.html" ,name = course["CourseName"], code = course["CourseCode"], AttendedClasses=course["AttendedClasses"], TotalClasses=course["TotalClasses"])



@courses_bp.route("/add_course", methods=['GET', "POST"])
def add_course():
    if request.method == "GET":
        course_d = {
            "CourseCode" : "",
            "CourseName" : "",
            "TotalClasses" : "",
            "AttendedClasses" : ""
        }
        return render_template("courses/add_course.html",course_d = course_d)
    else:
        course_d = {}
        course_d["CourseCode"] = request.form.get('CourseCode')
        course_d["CourseName"] = request.form.get('CourseName')
        course_d["TotalClasses"] = request.form.get('TotalClasses')
        course_d["AttendedClasses"] = request.form.get('AttendedClasses')
        post = True
        course = Course()
        if post:
            u = course.add_course()
            if u:
                return redirect("/courses")
        error = "Course already exists"
        return render_template("courses/add_course.html",course_d = course_d, error = error), 400
        

@courses_bp.route("/update_course", methods=['GET', "POST"])
def update_course():
    if request.method == "GET":
        course_d = {
            "CourseCode" : "",
            "CourseName" : "",
            "TotalClasses" : "",
            "AttendedClasses" : ""
        }
        return render_template("courses/add_course.html",course_d = course_d)
    else:
        course_d = {}
        course_d["CourseCode"] = request.form.get('CourseCode')
        course_d["CourseName"] = request.form.get('CourseName')
        course_d["TotalClasses"] = request.form.get('TotalClasses')
        course_d["AttendedClasses"] = request.form.get('AttendedClasses')
        post = True
        course = Course()
        if post:
            u = course.add_course()
            if u:
                return redirect("/courses")
        error = "Course already exists"
        return render_template("courses/add_course.html",course_d = course_d, error = error), 400
        