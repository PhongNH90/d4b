from flask import Flask, request, render_template, redirect, flash, session
from models import mlab
from models.plugin import *
from models.user import User

app = Flask(__name__)
app.config["SECRET_KEY"] = "aajlajfkaf"
mlab.connect()


@app.route("/register", methods = ["GET", "POST"])
def register():
  if "token" not in session:
    if request.method == "GET":
      return render_template("register.html")
    else:
      form = request.form
      username = form["username"].lower() 
      password = form["password"]
      ck = check_username(username)
      if ck != True:
        flash (ck)
        return render_template("register.html")
      else:
        u = User(username=username, password=password, active=False )
        u.save()
        return render_template("get_info.html")
  else:
    return render_template("home.html")

@app.route("/register", methods = ["GET", "POST"])
def register():
  if "token" not in session:
    if request.method == "GET":
      return render_template("register.html")
    else:
      form = request.form
      username = form["username"].lower() 
      password = form["password"]
      ck = check_username(username)
      if ck != True:
        flash (ck)
        return render_template("register.html")
      else:
        u = User(username=username, password=password, active=False )
        u.save()
        session["token"] = str(user["id"])
        return render_template("get_info.html")
  else:
    return render_template("home.html")

@app.route("/get-info", methods = ["GET", "POST"])
def get_info():
  if "token" in session:
    user = User.objects.with_id(session["token"])
    if request.method == "GET":
      return render_template("get_info.html")
    else:
      form = request.form
      email = form["email"].lower() 
      facebook = form["facebook"]
      phone = form["phone"].lower() 
      d_birth = form["d_birth"]
      m_birth = form["m_birth"]
      y_birth = form["m_birth"]
      city = form["city"]
      img = form["avatar"]
      description = form["description"]
      
      u = User(em=email, facebook=facebook, phone active=False )
      u.save()
      session["token"] = str(user["id"])
      return render_template("get_info.html")
  else:
    return render_template("login.html")        

@app.route("/login", methods = ["GET", "POST"])
def login():
  if "token" not in session:
    if request.method == "GET":
      return render_template("login.html")
    elif request.method == "POST":
      form = request.form
      u = form["username"].lower()
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
  else:
    return redirect("/")

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
    user = User.objects.with_id(session["token"])
    user = place_img(user)
    user = place_stt(user)
    follow_list = []
    for i in user["follow_list"]:
      u = User.objects.with_id(i)
      u = place_img(u)
      u = place_stt(u)
      follow_list.append(u)
    print(follow_list)
    boy = list(User.objects(gender="male"))
    hot_boy = get_top(boy,"like",3)
    hotboy = []
    for u in hot_boy:
      hotboy.append(place_img(u))
    girl = list(User.objects(gender="female"))
    hot_girl = get_top(girl,"like",3)
    hotgirl = []
    for u in hot_girl:
      hotgirl.append(place_img(u))
    return render_template("index.html", user = user, follow_list=follow_list, hotboy=hotboy, hotgirl= hotgirl )
  else:
    return redirect("/login")

@app.route("/follow/<uid>")
def follow():
  if "token" in session:
    user = User.objects.with_id(session["token"])
    user["follow_list"].append(uid)
    user.save()
    user2 = User.objects.with_id(uid)
    user2["like"] += 1
    user2.save()

@app.route("/unfollow/<uid>")
def unfollow(uid):
  if "token" in session:
    user = User.objects.with_id(session["token"])
    l1 = user["follow_list"]
    l1.remove(uid)
    user.update(set__follow_list=l1)
    user.reload()
    user2 = User.objects.with_id(uid)
    l2 = 0
    user2.update(set__like=l2)
    user2.reload()
  return redirect("/")

@app.route("/search/<un>")
def search_user(un):
  if "token" in session:
    search_list = search(User.objects,un)
    return render_template("search.html", search_list=search_list)

@app.route("/suggest")
def suggest():
  if "token" in session:
    user = User.objects.with_id(session["token"])
    if user["gender"] == "male":
      list_u = User.objects(gender="female")
    else:
      list_u = User.objects(gender="male")
    suggest_list = suggest(user,list_u)
    return render_template("suggest.html",suggest_list=suggest_list)

@app.route("/profile/<uid>")
def profile(uid):
  if "token" in session:
    user =  user.objects.with_id("sesion")
    return render_template("profile.html", user = user)
    

if __name__ == '__main__':
  app.run(debug=True)