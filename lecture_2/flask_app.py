from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/about")
def about_us():
    return "Information about us"


@app.route("/greeting/<string:name>")
def greeting(name):
    return "Welcome " + name + ", how are you"


@app.route("/add", methods=['GET'])
def add():
    n1 = int(request.args.get("n1", 0))
    n2 = int(request.args.get("n2", 0))
    s = n1 + n2
    return str(s)


@app.route("/add_post", methods=['POST'])
def add_post():
    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])
    s = n1 + n2
    return str(s)


@app.route("/div_post", methods=['POST'])
def div_post():
    n1 = int(request.form["n1"])
    n2 = int(request.form["n2"])
    if n2 == 0:
        abort(400)
    s = n1 / n2
    return str(s)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
