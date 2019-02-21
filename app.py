from flask import Flask, redirect, request, render_template, flash, session
# import mlab

app = Flask(__name__)

@app.route('/dating4banker', methods = ["GEt", "POST"])
def home():
  if request.method == "GET":
    return render_template("login.html")
  else:
    return "Hello"
  

if __name__ == '__main__':
  app.run(debug=True)