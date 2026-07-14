from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Cookie Example</h2>
    <form action="/setcookie" method="POST">
        Name: <input type="text" name="username">
        <input type="submit" value="Submit">
    </form>
    """

@app.route("/setcookie", methods=["POST"])
def setcookie():
    username = request.form["username"]
    res = make_response("<h3>Cookie Saved Successfully!</h3><a href='/getcookie'>View Cookie</a>")
    res.set_cookie("username", username)
    return res

@app.route("/getcookie")
def getcookie():
    username = request.cookies.get("username")
    return f"<h3>Welcome, {username}</h3>"

if __name__ == "__main__":
    app.run(debug=True)