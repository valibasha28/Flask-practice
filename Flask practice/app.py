from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome to Flask </h1>"

@app.route("/courses")
def courses():
    return " Welcome to our courses "

@app.route("/<name>")
def name(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect('/')

@app.route('/url')
def url():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)