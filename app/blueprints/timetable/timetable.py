from flask import Blueprint, render_template, redirect, session, jsonify, request
import json
from app.login_required import login_required
timetable_bp = Blueprint("timetable", __name__, template_folder="templates",static_folder="static")

@timetable_bp.route("/", methods=["GET", "POST"])
@login_required
def timetable():
    from app import db
    user_id = session["user_id"]
    list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    slots = db.user.find_one({"_id":user_id}, {"slots":1, "_id":0})['slots']
    timetable = db.user.find_one({"_id":user_id}, {"timetable":1, "_id":0})['timetable']
    if(request.method == "POST"):
        if 'UpdateTable' in request.form:
            timetable_data=json.loads(request.form.get("timetable"))
            
            db.user.update_one( {"_id":user_id},
                {
                    "$set": {
                    "timetable": timetable_data
                    }
                }
            )
            timetable = timetable_data
        else:
            new_slots = request.form.get("slots_value")
            db.user.update_one( {"_id":user_id},
                {
                    "$set": {
                    "slots": new_slots
                    }
                }
            )
            if int(slots) > int(new_slots):
                for i in range(int(new_slots), int(slots)):
                    for day in list:
                        del timetable[day + str(i)]
            
            slots = new_slots

    for day in list:
        for i in range(int(slots)):
            if day + str(i) not in timetable:
                timetable[day + str(i)]= "None"
    db.user.update_one( {"_id":user_id},
        {
            "$set": {
            "timetable": timetable
            }
        }
    )         
    courses = db.user.find_one({"_id": user_id},{"courses":1,"_id":0})['courses']

    return render_template("timetable.html", courses = courses, slots=slots, timetable=timetable, list = list)