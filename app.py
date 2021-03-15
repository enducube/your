import eventlet
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@socketio.on("connect")
def connect():
    emit("message","a new user has connected.",broadcast=True)

@socketio.on("disconnect")
def disconnect():
    emit("message","a user has disconnected.",broadcast=True)

@socketio.on("msg")
def bruh(json):
    emit("message",str(json),broadcast=True)
    pass
if __name__ == '__main__':
    print("bar")
    socketio.run(app)