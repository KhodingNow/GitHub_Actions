from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() #take environment varaiables frm .env

app = Flask(__name__)

@app.route('/<random_string>')
def return_backwards_string(random_string):

    return "".join(reversed(random_string))


@app.route('/get-mode')
def get_mode():
    return os.environ.get("MODE")

if __name__ == 'main':
    return_backwards_string