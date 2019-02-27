from flask import Flask, render_template

app = Flask(__name__)

def create_article(name, description, price):
    return {
        "name": name,
        "description": description,
        "price": price
    }

articles = [
    create_article("Guitar", "Fender Telecaster", 1200),
    create_article("Bass", "Fender P-bass", 1500),
    create_article("Bass strings", "Elixir 50-130", 50)
]


@app.route("/")
def shop():
    return render_template("shop.html", items=articles)

app.run()
