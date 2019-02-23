from flask import Flask

app = Flask('test')

@app.route("/register")
def register():
    res = """
    <html>
        <head><title>just test</title></head>
    """
    res += "<body>"

    for i in range(1, 7):
        res += f"<h{i}>register</h{i}>"
    
    res += """
    </body>
    </html>
    """
    return res

@app.route("/test")
def test():
    with open("test.html") as f:
        content = str().join(f.readlines())
        return content

if __name__ == "__main__":
    app.run()
