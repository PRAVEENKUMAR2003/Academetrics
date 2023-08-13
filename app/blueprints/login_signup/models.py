from flask import jsonify, request, session, redirect
import uuid
import bcrypt


class User:
    
    def exists(email):
        from app import db
        user = db.user.find_one({"email":email})
        if user:
            return True
        return False
    
    def check_password():
        from app import db
        user = db.user.find_one({"_id": session['user_id']})
        if user:
            if bcrypt.checkpw(request.form.get('cur_password').encode(), user["password"].encode()):
                return True
        return False
    
    def change_password():
        from app import db
        user = db.user.find_one({"_id": session['user_id']})
        db.user.update_one({"_id": session['user_id']},{'$set':{'password':bcrypt.hashpw(request.form.get('new_password').encode('utf-8'), bcrypt.gensalt()).decode()}})
        
    
    def check():
        from app import db
        user = db.user.find_one({"email":request.form.get('email')})
        if user:
            if bcrypt.checkpw(request.form.get('password').encode(), user["password"].encode()):
                return user
        return None
    def delete():
        from app import db
        db.user.delete_one({"_id": session['user_id']})
        
    
    def login(user):
        session["logged_in"] = True
        session["username"] = user["username"]
        session["email"] = user["email"]
        session["user_id"] = user["_id"]
    
    def logout():
        session.clear()
        
    def signup(username,email):
        from app import db
        user = {
            "_id": uuid.uuid4().hex,
            "username": username,
            "email": email,
            "password":  bcrypt.hashpw(request.form.get('password').encode('utf-8'), bcrypt.gensalt()).decode(),
            "courses": [],
            "tasks": [],
            "slots": "1",
            "timetable":{'Sunday0':"None",'Monday0':"None",'Tuesday0':"None",'Wednesday0':"None",'Thursday0':"None",'Friday0':"None",'Saturday0':"None",}
            
        }


        if db.user.insert_one(user):
            return user
        return None
