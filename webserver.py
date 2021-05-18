from flask import Flask
from threading import Thread
import socket

app = Flask('')

@app.route('/')
def home():
  ip = socket.gethostbyname(socket.gethostname())
  return ("Pinging to " + ip)

def run():
  app.run(host='0.0.0.0',port=8080)

def refresh():
    t = Thread(target=run)
    t.start()
