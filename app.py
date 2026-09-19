from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/front_page")

@app.route("/front_page")
def form():
    return render_template("page.html", front_page=True)


#@app.route("/result", methods=["POST"])
#def result():
#    message = request.form["message"]
#    return render_template("result.html", message=message)

#@app.route("/order")
#def order():
#    return render_template("order.html")

#@app.route("/order_result", methods=["POST"])
#def order_result():
#    pizza = request.form["pizza"]
#    extras = request.form.getlist("extra")
#    message = request.form["message"]
#    return render_template("result.html", pizza=pizza, extras=extras, message=message)
    
