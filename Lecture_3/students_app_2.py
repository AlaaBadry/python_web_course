from flask import Flask, jsonify, abort, request

app = Flask(__name__)


students = [
    {"id": 555, "name": "Ahmad", "birth_year": 1990}
]


###############################

@app.route("/students/", methods=['GET'])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=['GET'])
def get_student(student_id):
    for item in students:
        if item["id"] == student_id:
            return jsonify(item)
    else:
        abort(404, "student not found")


@app.route("/students/", methods=['POST'])
def insert_student():
    if not request.content_type == 'application/json':
        abort(400, "content type must be application/json")
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "success"}), 201


@app.route("/students/<int:student_id>", methods=['PUT'])
def update_student(student_id):
    if not request.content_type == 'application/json':
        abort(400, "content type must be application/json")
    data = request.get_json()
    for x in range(len(students)):
        if students[x]["id"] == student_id:
            del students[x]
            students.append(data)
            return jsonify({"message": "success"})
    else:
        abort(404, "student not found")


@app.route("/students/<int:student_id>", methods=['DELETE'])
def delete_student(student_id):
    for x in range(len(students)):
        if students[x]["id"] == student_id:
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
