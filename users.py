from flask import Flask, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import db 
from utils import * #redirection

from init import app


@app.route("/log_in", methods=["POST"])
def log_in():
  username = get_non_empty("username", "empty_username")
  if not username: 
    if "log_in_attempt" in session:
      del session["log_in_attempt"]
    return redirection()
  session["log_in_attempt"] = username

  password = get_non_empty("password", "empty_password")
  if not password: return redirection()

  sql = "SELECT id, password_hash FROM Users WHERE username = ?"
  query = db.query(sql, [username])
  if not query:
    session["incorrect_username"] = True
    return redirection()
  query = query[0]
  password_hash = query[1]

  if check_password_hash(password_hash, password):
    session["username"] = username
    session["user_id"] = query[0]
    clear_login_attempt()
    return redirection()
  else:
    session["incorrect_password"] = True
    return redirection()

def clear_login_attempt():
  if "log_in_attempt" in session:
    del session["log_in_attempt"] 
  if "incorrect_username" in session:
    del session["incorrect_username"] 
  if "incorrect_password" in session:
    del session["incorrect_password"] 


@app.route("/log_out")
def log_out():
  del session["username"]
  del session["user_id"]
  return redirection()

@app.route("/sign_in")
def sign_in():
  clear_login_attempt()
  session["sign_in"] = True
  return redirection()

@app.route("/cancel_sign_in")
def cancel_sign_in():
  clear_sign_in_attempt()
  return redirection()

def clear_sign_in_attempt():
  if "sign_in" in session:
    del session["sign_in"] 
  if "sign_in_attempt" in session:
    del session["sign_in_attempt"]
  if "no_match" in session:
    del session["no_match"]
  if "name_not_available" in session:
    del session["name_not_available"]
  if "empty_username" in session:
    del session["empty_username"]
  if "empty_password" in session:
    del session["empty_password"]



@app.route("/register", methods=["POST"])
def register():
  username = get_non_empty("username", "empty_username")
  if not username: return redirection()

  password = get_non_empty("password", "empty_password")
  if not password: return redirection()

  password2 = request.form["password2"]
  
  if password != password2:
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

  password_hash = generate_password_hash(password)
  try:
    sql = "INSERT INTO Users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])
  except sqlite3.IntegrityError:
    print("Error while trying to sign in")
    return redirection()
  
  clear_sign_in_attempt()
  return redirection()

@app.route("/delete_user")
def delete_user():
  delete_user_sql = "DELETE FROM Users WHERE username = ?"
  db.execute(delete_user_sql, [session["username"]])
  delete_posts_sql = "DELETE FROM Posts WHERE poster = ?"
  db.execute(delete_posts_sql, [session["user_id"]])
  delete_comments_sql = "DELETE FROM Comments WHERE commenter_id = ?"
  db.execute(delete_comments_sql, [session["user_id"]])
  del session["username"]
  del session["user_id"]
  return redirection()
