from flask import Flask, redirect, request, render_template, session, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import base64
import sqlite3
import db 
from utils import *
import users
import datetime

from init import app


@app.route("/")
def index():
  return redirect("/front_page")

@app.route("/set_sorting")
def set_sorting():
  return redirect("/front_page")


@app.route("/front_page")
def front_page():
  session["page"] = "/front_page"

  sql = '''
      SELECT B.username, A.id, A.title, A.post_date
      FROM Posts A
      LEFT JOIN Users B ON B.id = A.poster
      ORDER BY A.post_date ASC;
    '''
  query = db.query(sql, [])
  posts = multi_list(query, list(range(0,4)))
  return render_template("page.html", posts=posts)


@app.route("/image/<int:post_id>")
def get_image(post_id):
  sql = "SELECT image_data FROM Posts WHERE id = ?"
  image = db.query(sql, [post_id])[0][0]
  response = make_response(bytes(image))
  response.headers.set("Content-Type", "image/jpeg")
  return response

@app.route("/post/<int:post_id>")
def post_page(post_id):
  session["page"] = "/post/" + str(post_id)
  sql = '''
      SELECT B.username, A.id, A.title, A.post_date
      FROM Posts A
      LEFT JOIN Users B ON B.id = A.poster
      WHERE A.id = ?
    '''
  post = db.query(sql, [post_id])[0]
  return render_template("page.html", post = post)

@app.route("/new_post")
def new_post():
  if not "username" in session:
    return redirect("/front_page")
  session["previous_page"] = session["page"]  
  session["page"] = "/new_post"
  return render_template("page.html")

@app.route("/create_post", methods = ["POST"])
def create_post():
  title = get_non_empty("title", "empty_title")
  if not title: return redirection()

  tags = get_non_empty("tag_list", "empty_tag_list")
  if not tags: return redirection()
 
  tag_list = [item.strip() for item in tags.split(',')]

  file = request.files["image"]
  if not (file.filename.endswith(".jpg") or file.filename.endswith(".png")):
    return "VIRHE: väärä tiedostomuoto"

  image = file.read()

  user_id = session["user_id"]
  post_date = datetime.datetime.now()

  sql = "INSERT INTO Posts (title, poster, post_date, image_data) VALUES (?, ?, ?, ?)"
  db.execute(sql, [title, user_id, post_date, image])

  return go_back()

@app.route("/delete_post", methods = ["POST"])
def delete_post():
  post_id = request.form["post_id"] 
  sql = "DELETE FROM Posts WHERE id = ?"
  db.execute(sql, [post_id])
  # TODO kommentit ja avainsanat poistettava myös, jahka totetutetaan.
  return redirect("/front_page")


def go_back(): 
  if "previous_page" in session: 
    if session["page"] == session["previous_page"]: 
      del session["previous_page"] 
      return redirect("/front_page")
    session["page"] = session["previous_page"] 
    del session["previous_page"] 
    return redirection()
  return redirect("/front_page")

@app.route("/cancel_post")
def cancel_post():
  return go_back()

