from flask import Flask, jsonify, abort, request
from student import Student

app = Flask(__name__)


students = [
    Student("10", "Ahmed", "Giza"),
    Student("11", "Hany", "Cairo"),
    Student("12", "Asmaa", "Alex")
]


###############################

@app.route("/students/", methods=["GET"])
def get_students():
    data = [item.to_json() for item in students]
    return jsonify(data)


@app.route("/students/<student_id>", methods=["GET"])
def get_student(student_id):
    for item in students:
        if item.id == student_id:
            return jsonify(item.to_json())
    else:
        abort(404, "student not found")


@app.route("/students/", methods=["POST"])
def insert_student():
    if not request.content_type == "application/json":
        abort(400, "content type must be application/json")
    data = request.get_json()
    student = Student.from_json(data)
    students.append(student)
    return jsonify({"message": "success"}), 201


@app.route("/students/", methods=["PUT"])
def update_student():
    if not request.content_type == "application/json":
        abort(400, "content type must be application/json")
    data = request.get_json()
    new_student = Student.from_json(data)
    for x in range(len(students)):
        if students[x].id == new_student.id:
            del students[x]
            students.append(new_student)
            return jsonify({"message": "success"})
    else:
        abort(404, "student not found")


@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    for x in range(len(students)):
        if students[x].id == student_id:
            del students[x]
            return jsonify({"message": "success"})
    else:
        abort(404, "student not found")


###############################

@app.errorhandler(404)
@app.errorhandler(400)
def on_error(error):
    return jsonify({"message": error.description}), error.code


###############################

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
