from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<user>")
def hello(user):
    return render_template("hello.html", user=user)

app.run()
