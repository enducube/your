import eventlet
from flask import Flask, render_template, g
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import flask_login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/stuff.db'
socketio = SocketIO(app)
db = SQLAlchemy(app)
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    flask_login.UserMixin()

@login_manager.user_loader
def load_user(user_id):
    return User.get


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
    emit("reload",broadcast=True)


if __name__ == '__main__':
    print("bark 127.0.0.1:5000/")
    socketio.run(app)