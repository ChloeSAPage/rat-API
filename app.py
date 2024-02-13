from flask import Flask, send_file, render_template
import glob

app = Flask(__name__)


@app.route("/get-rat/<rat_id>")
def get_rat(rat_id):

    rat_pic_path = f"resources/rat{rat_id}.jpg"
    
    num_rat_pics = len(glob.glob("resources/*.jpg"))

    try:
        return send_file(rat_pic_path, mimetype="image/jpeg"), 200
    except FileNotFoundError:
        return render_template("error.html", amount=num_rat_pics), 404, {"Description": f"MAX Rat ID is 0{num_rat_pics}"}


if __name__ == "__main__":
    app.run(debug=True)