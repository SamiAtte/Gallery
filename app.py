from flask import Flask, redirect, request, render_template, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import db 
#import config
import utils
import users

from init import app

#app = Flask(__name__)
#app.secret_key = config.secret_key

@app.route("/")
def index():
  return redirect("/front_page")

@app.route("/front_page")
def front_page():
  session["page"] = "/front_page"
  return render_template("page.html")


@app.route("/post/<int:post_id>")
def post_page(post_id):
  session["page"] = "/post_page/" + str(post_id)
  return render_template("page.html")


