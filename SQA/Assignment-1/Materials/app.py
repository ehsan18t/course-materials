# app.py
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

students = [
    {"id": 1, "name": "Abdul Jabbar", "personnummer": "920223-9999", "courses_passed": [
        "CSE2213", "CSE1110", "CSE1111", "CSE1114", "CSE1115", "CSE1116", "CSE2117", "CSE2118", "CSE3119", "CSE4010"]},
    {"id": 2, "name": "Abdel Ahmed", "personnummer": "990111-9999", "courses_passed": [
        "CSE2213", "CSE1110", "CSE1111", "CSE1114", "CSE1115", "CSE1116", "CSE2117"]},
    {"id": 3, "name": "Joel Stevensson ",
        "personnummer": "011030-9999", "courses_passed": []},
    {"id": 4, "name": "Yue Sakamoto", "personnummer": "980401-9999", "courses_passed": [
        "DSE1001", "DSEE1002", "DSE1003", "DSE1004", "DSE2105", "DSE2116", "DSE3217", "DSE3218", "DSE3239", "DSE4100"]},
    {"id": 5, "name": "Ivan Faknamovich", "personnummer": "951128-9999",
        "courses_passed": ["DSE1001", "DSE1002", "DSE1003", "DSE3217"]},
    {"id": 6, "name": "Amy Pond", "personnummer": "020201-9999", "courses_passed": [
        "CSE2213", "CSE1110", "CSE1111", "CSE1114", "CSE1115", "CSE1116", "CSE2117", "CSE2118", "CSE3119", "CSE4010", "DSE1004", "DSE2105"]},
    {"id": 7, "name": "Rory Williams", "personnummer": "010203-9999", "courses_passed": [
        "CSE1115", "CSE4010", "DSE1001", "DSE1002", "DSE1003", "DSE1004", "DSE2105", "DSE2116", "DSE3217", "DSE3218", "DSE3239", "DSE4100"]},
    {"id": 8, "name": "Steve Rogers", "personnummer": "07045-9999",
        "courses_passed": ["CSE1115", "CSE4010", "DSE1001", "DSE1004", "DSE2105", "DSE1004"]},
    {"id": 9, "name": "Natasha Romanov",
        "personnummer": "861231-9999", "courses_passed": ["CSE2213"]}
]

programs = [
    {"id": 1, "courses_required": ["CSE2213", "CSE1110", "CSE1111", "CSE1114",
                                   "CSE1115", "CSE1116", "CSE2117", "CSE2118", "CSE3119", "CSE4010"]},
    {"id": 2, "courses_required": ["DSE1001", "DSE1002", "DSE1003", "DSE1004",
                                   "DSE2105", "DSE2116", "DSE3217", "DSE3218", "DSE3239", "DSE4100"]}
]


def _find_next_id():
    return max(student["id"] for student in students) + 1


@app.get("/student")
def get_students():
    return jsonify(students)


@app.get("/student/<id>")
def get_student(id):
    try:
        int(id)
    except:
        return {"error": "Student ID " + id + " is not formatted correctly."}, 400

    for student in students:
        if student["id"] == int(id):
            return jsonify(student)
    return {"error": "Student ID " + id + " does not exist"}, 404


@app.post("/create")
def add_student():
    if request.is_json:
        student = request.get_json()
        student["id"] = _find_next_id()

        # name, personnummer must exist
        # check format of both
        if "name" not in student:
            return {"error": "No name field"}, 400
        elif student["name"] == "" or student["name"] == None:
            return {"error": "Blank or null name"}, 400

        if "personnummer" not in student:
            return {"error": "No personnummer field"}, 400
        elif student["personnummer"] == "" or student["personnummer"] == None:
            return {"error": "Blank or null personnummer"}, 400

        pattern = re.compile(r'^\d{6}-\d{4}$')
        if pattern.match(student["personnummer"]):
            month = int(student["personnummer"][2:4])
            day = int(student["personnummer"][4:6])
            if month == 0 or month > 12:
                return {"error": "Invalid month in personnummer"}, 400
            if day == 0 or day > 31:
                return {"error": "Invalid day in personnummer"}, 400
        else:
            return {"error": "Malformed personnummer " + student["personnummer"]}, 400

        for existing in students:
            if student["personnummer"] == existing["personnummer"]:
                return {"error": "Personnummer already belongs to student " + str(existing["id"])}, 400

        # check format of courses
        if "courses_passed" in student:
            for course in student["courses_passed"]:
                if course == "" or course == None:
                    return {"error": "Empty or null course ID"}, 400

                pattern = re.compile(r'^[a-zA-Z]{3}\d{4}$')
                if not pattern.match(course):
                    return {"error": "Malformed course ID: " + course}, 400
        # no courses passed is ok, can be added as empty
        else:
            student["courses_passed"] = []

        # other fields scrubbed
        for key in student:
            if key != "id" and key != "personnummer" and key != "name" and key != "courses_passed":
                del student[key]
        # insert into database if all checks pass
        students.append(student)

        return student, 201
    return {"error": "Request must be JSON-formatted"}, 415


@app.put("/update/<id>")
def update_student(id):
    try:
        int(id)
    except:
        return {"error": "Student ID " + id + " is not formatted correctly."}, 400

    if request.is_json:
        student = request.get_json()
        student["id"] = id

        # name, personnummer must exist
        # check format of both
        if "name" not in student:
            return {"error": "No name field"}, 400
        elif student["name"] == "" or student["name"] == None:
            return {"error": "Blank or null name"}, 400

        if "personnummer" not in student:
            return {"error": "No personnummer field"}, 400
        elif student["personnummer"] == "" or student["personnummer"] == None:
            return {"error": "Blank or null personnummer"}, 400

        pattern = re.compile(r'^\d{6}-\d{4}$')
        if pattern.match(student["personnummer"]):
            month = int(student["personnummer"][2:4])
            day = int(student["personnummer"][4:6])
            if month == 0 or month > 12:
                return {"error": "Invalid month in personnummer"}, 400
            if day == 0 or day > 31:
                return {"error": "Invalid day in personnummer"}, 400
        else:
            return {"error": "Malformed personnummer " + student["personnummer"]}, 400

        # check format of courses
        if "courses_passed" in student:
            for course in student["courses_passed"]:
                if course == "" or course == None:
                    return {"error": "Empty or null course ID"}, 400

                pattern = re.compile(r'^[a-zA-Z]{3}\d{4}$')
                if not pattern.match(course):
                    return {"error": "Malformed course ID: " + course}, 400
        # no courses passed is ok, can be added as empty
        else:
            student["courses_passed"] = []

        # other fields scrubbed
        for key in student:
            if key != "id" and key != "personnummer" and key != "name" and key != "courses_passed":
                del student[key]

        # Passed format checks. Find the correct record and update.
        found = False
        for existing in students:
            if existing["id"] == int(id):
                found = True
                if existing["personnummer"] != student["personnummer"]:
                    return {"error": "Changes to personnummer are not allowed."}, 400
                else:
                    existing["name"] = student["name"]
                    existing["courses_passed"] = student["courses_passed"]

            elif student["personnummer"] == existing["personnummer"]:
                return {"error": "Personnummer already belongs to student " + str(existing["id"])}, 400

        if found:
            return student, 200
        else:
            return {"error": "Student ID " + id + " does not exist"}, 404
    return {"error": "Request must be JSON-formatted"}, 415


@app.delete("/delete/<id>")
def delete_student(id):
    try:
        int(id)
    except:
        return {"error": "Student ID " + id + " is not formatted correctly."}, 400

    for student in students:
        if student["id"] == int(id):
            return {"deleted": id}
    return {"error": "Student ID " + id + " does not exist"}, 404


@app.get("/program")
def get_programs():
    return jsonify(programs)


@app.get("/program/<id>")
def get_program(id):
    try:
        int(id)
    except:
        return {"error": "Program ID " + id + " is not formatted correctly."}, 400

    for program in programs:
        if program["id"] == int(id):
            return jsonify(program)
    return {"error": "Program ID " + id + " does not exist"}, 404


@app.get("/finished/<student_id>/<program_id>")
def is_finished(student_id, program_id):
    try:
        int(student_id)
    except:
        return {"error": "Student ID " + student_id + " is not formatted correctly."}, 400
    try:
        int(program_id)
    except:
        return {"error": "Program ID " + program_id + " is not formatted correctly."}, 400

    for student in students:
        if student["id"] == int(student_id):
            for program in programs:
                if program["id"] == int(program_id):
                    matching_courses = 0
                    all_courses = True
                    for course in program["courses_required"]:
                        if course in student["courses_passed"]:
                            matching_courses += 1
                        else:
                            all_courses = False

                    return {"status": all_courses, "completed_courses": matching_courses}, 200
            return {"error": "Program ID " + program_id + " does not exist"}, 404
    return {"error": "Student ID " + student_id + " does not exist"}, 404
