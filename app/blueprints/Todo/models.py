from flask import jsonify, request, session
import uuid

class Course:
    
    def add_course(self):
        from app import db
        course = {
            "TodoDescription" : request.form.get('TodoDescription'),
            "TodoName" : request.form.get('TodoName'),
            "TodoDeadline" : request.form.get('TodoDeadline')
        }
        try: 
            db.user.find_one({"_id": session['user_id']},{"tasks":{"$elemMatch": {"TodoName":course["TodoName"]}}})['tasks'][0]
        except:
            db.user.update_one({"_id": session['user_id']}, {'$push': {'tasks':course}})
            return course
        return None

        
    def course_list(self):
        from app import db
        course = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        course = db.user.find_one({"_id": session['user_id']},{"tasks":1})['tasks']
        return course
        
    def course_details(self,name):
        from app import db
        course = {
            "TodoDescription" : "",
            "TodoName" : "",
            "TodoDeadline" : ""
        }
        course = db.user.find_one({"_id": session['user_id']},{"tasks":{"$elemMatch": {"TodoName":name}}})['tasks'][0]
        return course
