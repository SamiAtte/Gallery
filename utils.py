from flask import Flask, redirect, session

def redirection(): 
  if "page" in session:
    return redirect(session["page"])
  return redirect("/front_page")


