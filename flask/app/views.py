from app import app
import os
from flask import Flask, render_template

@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        pass
    else:
        app_name = "Not Found - 404"

    return render_template("public/start.html", name=app_name)


@app.route("/api/v1")
def api():
    return {
        "result": "Base API Endpoint",
        "status": 200
    }