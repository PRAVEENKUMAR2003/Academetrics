from flask import jsonify, request, session
import uuid
import bcrypt


class User:
    
    def exists(self):
        from app import db
        user = db.user.find_one({"email":request.form.get('email')})
        if user:
            return True
        return False
    
    def check(self):
        from app import db
        password = request.form.get('password')
        user = db.user.find_one({"email":request.form.get('email')})
        if user:
            if bcrypt.checkpw(password.encode(), user["password"].encode()):
                return user
        return None
    
    def login(self, user):
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
    
    def logout(self):
        session.clear()
        
    def signup(self):
        from app import db
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        user['password'] = bcrypt.hashpw(user['password'].encode('utf-8'), bcrypt.gensalt()).decode()

        if db.user.insert_one(user):
            return user
        return None
