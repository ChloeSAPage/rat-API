from flask import Flask, send_file, render_template, jsonify
import glob
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-rat/<rat_id>")
def get_rat(rat_id):

    rat_pic_path = f"resources/rat{rat_id}.jpg"
    num_rat_pics = len(glob.glob("resources/*.jpg"))

    try:
        return send_file(rat_pic_path, mimetype="image/jpeg"), 200
    except FileNotFoundError:
        return render_template("error.html", amount=num_rat_pics), 404, {"Description": f"MAX Rat ID is 0{num_rat_pics}"}


@app.route("/get-pic-amount")
def get_pic_amount():
    num_rat_pics = len(glob.glob("resources/*.jpg"))
    return str(num_rat_pics), 200


@app.route("/get-rat-facts")
def get_rat_fact():
    with open("ratfacts.json", "r") as f:
        rat_facts = json.load(f)
    return jsonify(rat_facts)


if __name__ == "__main__":
    app.run(debug=True)
