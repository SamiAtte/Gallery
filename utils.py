from flask import Flask, redirect, session, request

def get_non_empty(field : str, error : str) -> str:
  val = request.form[field]
  if not val:
    session[error] = True
  elif error in session:
    del session[error]
  return val


def redirection(): 
  if "page" in session:
    return redirect(session["page"])
  return redirect("/front_page")

def multi_list(query,ixt):
  mlist = []
  if query:
    for x in query:
      element = []
      for i in ixt:
        element.append(x[i])
      mlist.append(element)
  return mlist


