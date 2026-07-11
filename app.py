from flask import Flask, render_template, request, redirect, url_for, session
import os
from werkzeug.utils import secure_filename

from medicine_ai import get_medicine_info

from config import UPLOAD_FOLDER, RESULT_FOLDER, ALLOWED_EXTENSIONS

from database import (
    create_tables,
    register_user,
    login_user,
    save_medicine,
    get_all_medicines
)

from ocr import extract_text
from extract_medicine import extract_medicine_names
from search_serper import search_medicine
from scraper import scrape_apollo


app = Flask(__name__)

app.secret_key = "mediai_secret_key"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

create_tables()


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        success = register_user(name, email, password)

        if success:
            return redirect(url_for("login"))

        return "Email already exists"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = login_user(email, password)

        if user:
            session["user_id"] = user["id"]
            session["name"] = user["name"]
            session["email"] = user["email"]

            return redirect(url_for("dashboard"))

        return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["name"],
        email=session["email"]
    )


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        if "prescription" not in request.files:
            return "No file uploaded"

        file = request.files["prescription"]

        if file.filename == "":
            return "Please select a prescription image"

        if not allowed_file(file.filename):
            return "Only PNG, JPG, JPEG, WEBP files are allowed"

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        extracted_text = extract_text(filepath)

        medicines = extract_medicine_names(extracted_text)

        results = []

        for medicine in medicines:

            product_url = search_medicine(medicine)

            if product_url is None:
                details = {
                    "medicine_name": medicine,
                    "price": "Not Found",
                    "availability": "Unavailable",
                    "manufacturer": "-",
                    "pharmacy": "Not Found",
                    "product_url": "",
                    "ai_info": get_medicine_info(medicine)
                }

                save_medicine(details)
                results.append(details)
                continue

            details = scrape_apollo(product_url)

            details["medicine_name"] = medicine
            details["ai_info"] = get_medicine_info(medicine)
            details["product_url"] = product_url

            if not details.get("availability"):
                details["availability"] = "Available"

            if "1mg.com" in product_url:
                details["pharmacy"] = "Tata 1mg"

            elif "apollopharmacy.in" in product_url:
                details["pharmacy"] = "Apollo Pharmacy"

            elif "netmeds.com" in product_url:
                details["pharmacy"] = "NetMeds"

            elif "pharmeasy.in" in product_url:
                details["pharmacy"] = "PharmEasy"

            else:
                details["pharmacy"] = "Online Pharmacy"

            if details.get("price") != "Not Found" and product_url:
                details["availability"] = "Available"
            else:
                details["availability"] = "Unavailable"

            if not details.get("manufacturer"):
                details["manufacturer"] = "-"

            save_medicine(details)

            results.append(details)

        return render_template(
            "analysis.html",
            medicines=results,
            extracted_text=extracted_text
        )

    return render_template("upload.html")


@app.route("/availability")
def availability():

    if "user_id" not in session:
        return redirect(url_for("login"))

    medicines = get_all_medicines()

    return render_template(
        "availability.html",
        medicines=medicines
    )


@app.route("/medicine/<int:id>")
def medicine_details(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    medicines = get_all_medicines()

    for medicine in medicines:

        if medicine["id"] == id:

            return render_template(
                "pharmacy-details.html",
                medicine=medicine
            )

    return "Medicine Not Found"


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )