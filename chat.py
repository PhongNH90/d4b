from flask import Flask, render_template ,request , redirect
from flask_socketio import SocketIO,emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

# @app.route('/profile' , methods =["GET","POST"])
# def profile():
#     if request.method=="GET":
#         return render_templace("profile.html")
#     elif request.method =="POST":
#         return redirect("/chat_room")

@app.route('/chat_room')
def chat_room():
    return render_template("chat.html")

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, debug=True)