from flask import Flask, request, render_template, redirect, flash, session
from models import mlab
from models.user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "aajlajfkaf"
mlab.connect()



@app.route("/login", methods = ["GET", "POST"])
def login():
  if request.method == "GET":
    return render_template("login.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["password"]
    user = User.objects(username=u).first()
    if user != None:
      if user.password == p:
        session["token"] = str(user["id"])
        return redirect("/")
      else:
        flash("Invalid Password")
        return render_template("login.html")
    else:
      flash("User not found")
      return render_template("login.html")


@app.route("/logout")
def logout():
  if "token" in session:
    del session["token"]
    return redirect("/login")
  else:
    return redirect("/login")


@app.route("/")
def home():
  if "token" in session:
    return render_template("home.html", )
  else:
    return redirect("/login")



if __name__ == '__main__':
  app.run(debug=True)