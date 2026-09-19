from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import db 
from utils import redirection

from init import app

@app.route("/log_in", methods=["POST"])
def log_in():
  username = request.form["username"]
  password = request.form["password"]

  sql = "SELECT id, password_hash FROM Users WHERE username = ?"
  query = db.query(sql, [username])
  if not query:
    session["log_in_error"] = True
    return redirection()
  query = query[0]
  password_hash = query[1]

  if check_password_hash(password_hash, password):
    session["username"] = username
    session["user_id"] = query[0]
    if "log_in_error" in session:
      del session["log_in_error"] 
    return redirection()
  else:
    session["log_in_error"] = True
    return redirection(session)

@app.route("/log_out")
def log_out():
  del session["username"]
  del session["user_id"]
  return redirection()

@app.route("/sign_in")
def sign_in():
  session["sign_in"] = True
  return redirection()

@app.route("/cancel_sign_in")
def cancel_sign_in():
  del session["sign_in"] 
  if "sign_in_attempt" in session:
    del session["sign_in_attempt"]
  if "no_match" in session:
    del session["no_match"]
  if "name_not_available" in session:
    del session["name_not_available"]
  return redirection()



@app.route("/register", methods=["POST"])
def register():
  username  = request.form["username"]
  password1 = request.form["password1"]
  password2 = request.form["password2"]
  
  if password1 != password2:
    session["sign_in_attempt"] = username
    session["no_match"] = True
    return redirection()

  if "no_match" in session:
    del session["no_match"];
  sql = "SELECT 1 FROM Users WHERE username = ?"
  taken = db.query(sql, [username])
  if taken:
    print("Name taken.")
    session["sign_in_attempt"] = username
    session["name_not_available"] = True
    return redirection()

  password_hash = generate_password_hash(password1)
  try:
    sql = "INSERT INTO Users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])
  except sqlite3.IntegrityError:
    print("Error while trying to sign in")
    return redirection()
  
  if "no_match" in session:
    del session["no_match"];
  if "name_not_available" in session:
    del session["name_not_available"];
  if "sign_in_attempt" in session:
    del session["sign_in_attempt"];
  del session["sign_in"] 

  return redirection()


