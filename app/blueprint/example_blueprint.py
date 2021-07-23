from flask import Blueprint, render_template, request

geolocation_main = Blueprint("geolocation_main", __name__, template_folder='template')
geolocation = Blueprint("geolocation", __name__, template_folder='template')

@geolocation_main.route("/")
def get_location():
    return render_template('index.html')

@geolocation.route("/distance", methods=['POST'])
def get_distance():
    if request.method == 'POST':
        address = request.form["address"]
    return address
