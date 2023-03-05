from flask import Flask, render_template, request, redirect
import string
import random

app = Flask(__name__)

url_database = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shorten_url", methods=["POST"])
def shorten_url():
    long_url = request.form["long_url"]
    short_code = generate_short_code()
    url_database[short_code] = long_url
    short_url = request.host_url + short_code
    return render_template("shorten.html", short_url=short_url)

@app.route("/<string:short_code>")
def redirect_to_url(short_code):
    long_url = url_database.get(short_code)
    if long_url is None:
        return "Invalid URL"
    return redirect(long_url)

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

if __name__ == "__main__":
    app.run(debug=True)
