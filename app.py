import eventlet
from flask import Flask, render_template, g
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/stuff.db'
socketio = SocketIO(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer)
    username = db.Column(db.String)
    password = db.Column(db.String)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/int")
def internal():
    return render_template('int.html')

@socketio.on("connect")
def connect():
    pass

@socketio.on("disconnect")
def disconnect():
    pass

@socketio.on("click")
def bruh():
    g[0] += 1
    emit("reload",broadcast=True)
if __name__ == '__main__':
    print("bar 127.0.0.1:5000/")
    g.append(1)
    socketio.run(app)