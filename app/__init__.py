from flask import Flask, redirect
from flask_pymongo import PyMongo
from .blueprints.courses.courses import courses_bp
from .blueprints.login_signup.login_signup import login_signup_bp
from .blueprints.timetable.timetable import timetable_bp

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@academetricscluster.30t4yzc.mongodb.net/AcadDatabase"
app.config["SECRET_KEY"] = "Secret1234"
db = PyMongo(app).db

app.register_blueprint(courses_bp, url_prefix="/courses")
app.register_blueprint(login_signup_bp, url_prefix="/user")
app.register_blueprint(timetable_bp, url_prefix="/timetable")
