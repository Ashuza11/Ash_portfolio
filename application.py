
from flask import Flask, redirect,render_template, request

# Configure Application
app = Flask(__name__)

# All route
@app.route("/")
def index():
    """Show Home Page"""
    return render_template("index.html")


@app.route("/contact")
def contact():
    """Show Contact Page"""
    return render_template("/contact.html")

@app.route("/project")
def project():
    """Show Project Page"""
    return render_template("/project.html")

    
