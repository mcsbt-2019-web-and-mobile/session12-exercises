from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def shop():
    return render_template("child.html")

app.run()
