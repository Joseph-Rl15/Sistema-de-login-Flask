from flask import Blueprint, render_template

home_rota = Blueprint("home", __name__)


@home_rota.route("/")
def home():
    return render_template("index.html")
