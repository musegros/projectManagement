import random
from flask import Flask

app = Flask(__name__)

def coin_toss( ):
    return ['Heads', 'Tails'][random.randint(0,1)]

@app.route("/")
def hello():
    return "Hello, World!"
