#from flask import Flask, render_template
#from flask_socketio import SocketIO, send

#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret'
#socketio = SocketIO(app)

#@app.route('/')
#def index():
 #   return render_template('index.html')

#@socketio.on('message')
#def handleMessage(msg):
 #   print("Message:" + msg)
  #  send(msg, broadcast = True)

#if __name__ == '__main__':
 #   socketio.run(app)
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


# Routes to Render Something
@app.route('/')
def home():
  return render_template("home.html")


@app.route('/chat')
def chat():
  return render_template("chat.html")


@app.route('/accounts')
def about():
  return render_template("accounts.html")


# Make sure this we are executing this file
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
  app.run(debug=True)
  app.run(app)
