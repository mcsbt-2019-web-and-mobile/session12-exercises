from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def index():
    img = "img/coffee.jpg"

    return render_template("index.html", coffeeimg=img, names=["pepe", "antonio"])

@app.route("/css/<path>", methods = ["GET"])
def serve_css(path):
    return send_from_directory("css", path)

@app.route("/img/<path>", methods = ["GET"])
def serve_img(path):
    return send_from_directory("img", path)


app.run()
