from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("html", "index.html")

@app.route("/css/<path>", methods = ["GET"])
def serve_css(path):
    return send_from_directory("css", path)

@app.route("/img/<path>", methods = ["GET"])
def serve_img(path):
    return send_from_directory("img", path)


app.run()
