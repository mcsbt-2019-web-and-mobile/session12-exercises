from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<potato>")
def hello(potato):
    return render_template("hello.html", name=potato)

app.run()
