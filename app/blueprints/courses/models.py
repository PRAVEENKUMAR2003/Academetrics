from flask import jsonify, request, session
import uuid

class Course:
    
    def add_course(self):
        from app import db
        course = {
            "CourseCode" : request.form.get('CourseCode'),
            "CourseName" : request.form.get('CourseName'),
            "TotalClasses" : request.form.get('TotalClasses'),
            "AttendedClasses" : request.form.get('AttendedClasses')
        }
        try: 
            db.user.find_one({"_id": session['user_id']},{"courses":{"$elemMatch": {"CourseCode":course["CourseCode"]}}})['courses'][0]
        except:
            db.user.update_one({"_id": session['user_id']}, {'$push': {'courses':course}})
            return course
        return None

        
    def course_list(self):
        from app import db
        course = {
            "CourseCode" : "",
            "CourseName" : "",
            "TotalClasses" : "",
            "AttendedClasses" : ""
        }
        course = db.user.find_one({"_id": session['user_id']},{"courses":1})['courses']
        return course
        
    def course_details(self,name):
        from app import db
        course = {
            "CourseCode" : "",
            "CourseName" : "",
            "TotalClasses" : "",
            "AttendedClasses" : ""
        }
        course = db.user.find_one({"_id": session['user_id']},{"courses":{"$elemMatch": {"CourseCode":name}}})['courses'][0]
        return course

class Todo:
    def write_todo(self):
        from app import db
        todo = {
            "TodoDescription" : request.form.get('TodoDescription'),
            "TodoName" : request.form.get('TodoName'),
            "TodoDeadline" : request.form.get('TodoDeadline')
        }
    
        db.user.update_one({"_id": session['user_id']}, {'$push': {'todo':todo}})
        return todo

        
    def todo_list(self):
        from app import db
        todo = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        todo = db.user.find_one({"_id": session['user_id']},{"todo":1})['todo']
        return todo
        
    def todo_details(self,name):
        from app import db
        todo = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        todo = db.user.find_one({"_id": session['user_id']},{"todo":{"$elemMatch": {"TodoName":name}}})['todo'][0]
        return todo