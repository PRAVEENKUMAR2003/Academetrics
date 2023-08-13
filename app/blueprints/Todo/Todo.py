from flask import Blueprint, render_template, redirect, request
from .models import Course
todo_bp = Blueprint("Todo", __name__, template_folder="templates",static_folder="static")
from app.login_required import login_required


@todo_bp.route("/")
@login_required
def courses():
    list = Course().course_list()
    return render_template("courses/todos.html", list = list)

@todo_bp.route("/go_Todo/<id>")
@login_required
def go_course(id):
    course = Course().course_details(id)
    return render_template("courses/todo_page.html", name = course["TodoName"], description = course["TodoDescription"], deadline = course["TodoDeadline"])



@todo_bp.route("/add_Todo", methods=['GET', "POST"])
def add_course():
    if request.method == "GET":
        course_d = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        return render_template("courses/add_todo.html",course_d = course_d)
    else:
        course_d = {}
        course_d["TodoDescription"] = request.form.get('TodoDescription')
        course_d["TodoName"] = request.form.get('TodoName')
        course_d["TodoDeadline"] = request.form.get('TodoDeadline')
        post = True
        course = Course()
        if post:
            u = course.add_course()
            if u:
                return redirect("/todo")
        error = "Task already exists"
        return render_template("courses/add_todo.html",course_d = course_d, error = error), 400
        

@todo_bp.route("/update_Todo", methods=['GET', "POST"])
def update_course():
    if request.method == "GET":
        course_d = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        return render_template("courses/add_todo.html",course_d = course_d)
    else:
        course_d = {}
        course_d["TodoDescription"] = request.form.get('TodoDescription')
        course_d["TodoName"] = request.form.get('TodoName')
        course_d["TodoDeadline"] = request.form.get('TodoDeadline')
        post = True
        course = Course()
        if post:
            u = course.add_course()
            if u:
                return redirect("/todo")
        error = "Task already exists"
        return render_template("courses/add_todo.html",course_d = course_d, error = error), 400
        