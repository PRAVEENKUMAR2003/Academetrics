from flask import Blueprint, render_template, redirect, request
from .models import Todo
todo_bp = Blueprint("todo", __name__, template_folder="templates",static_folder="static")
from app.login_required import login_required


@todo_bp.route("/")
@login_required
def todo():
    list = Todo().todo_list()
    return render_template("to_do_list/to_do_list.html", list = list)

@todo_bp.route("/go_todo/<id>")
@login_required
def go_todo(id):
    todo = Todo().todo_details(id)
    return render_template("to_do_list/description.html" ,name = todo["TodoName"], description = todo["TodoDescription"], deadline = todo["TodoDeadline"])



@todo_bp.route("/write_todo", methods=['GET', "POST"])
def write_todo():
    if request.method == "GET":
        todo_d = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        return render_template("to_do_list/write_todo.html",todo_d = todo_d)
    else:
        todo_d = {}
        todo_d["TodoDescription"] = request.form.get('TodoDescription')
        todo_d["TodoName"] = request.form.get('TodoName')
        todo_d["TodoDeadline"] = request.form.get('TodoDeadline')
        post = True
        todo = Todo()
        if post:
            u = todo.write_todo()
            if u:
                return redirect("/todo")
        error = "Task already exists"
        return render_template("to_do_list/write_todo.html",todo_d = todo_d, error = error), 400
        
