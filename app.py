from flask import Flask, redirect, request, render_template, flash, session
from gmail import GMail, Message
import mlab
from models.user import User

app = Flask(__name__)
mlab.connect()


@app.route("/date4everyone/register", methods = ["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("register.html")
  else:
    form = request.form
    e = form["em"]  
    p = form["password"]
    name = form["name"]
    u = form["username"]
    g = form["gender"]
    b = form["birth"]
    i = form["img"]
    c = form["city"]
    h = form["hobby"]
    phone = form["phone"]
    des = form["description"]
    user_object = User.objects()
    if u in user_object:
      flash("Tên người dùng đã tồn tại")
      return render_template("/date4everyone")
    else:
      pass
    u = User(em=e, password=p, name=name, username=u, gender=g, birth=b, img=i, city=c, hobby=h, phone="+84"+phone, description=des)
    u.save()
    gmail = GMail('nguyenminhhieu2508@gmail.com','nguyenminhhieu')
    msg = Message('text', to = e, html = '<a href="http://127.0.0.1:5000/date4everyone">Xác nhận tài khoản</a>')
    gmail.send(msg)
    return "Register"

@app.route("/date4everyone", methods = ["GET", "POST"])
def home():
  if request.method == "GET":
    return render_template("home.html")
  elif request.method == "POST":
    form = request.form
    u = form["username"]
    p = form["password"]
    user = User.objects(username=u).first()
    if user != None:
      if user.password == p:
        session["token"] = u
        return redirect("/date4everyone")
      else:
        flash("Invalid Password")
        return redirect("/date4everyone")
    else:
      flash("User not found")
      return redirect("/date4everyone")
    

if __name__ == '__main__':
  app.run(debug=True)