"""
Tüm Flask route'larını merkezi bir modülde toplar.
"""
from flask import Blueprint, render_template, request, redirect, session
from user_auth import authenticate
from session_manager import create_session

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        role = authenticate(email, password)
        if role:
            create_session(email)
            session["email"] = email
            return redirect("/dashboard")
        else:
            return "Hatalı giriş bilgisi."
    return render_template("login.html")

@routes.route("/dashboard")
def dashboard():
    user = session.get("email")
    if user:
        return render_template("dashboard.html", user=user)
    return redirect("/")
