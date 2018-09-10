from app import app
from flask import Flask, flash, redirect, render_template, request, session, jsonify, make_response
import os



app = Flask(__name__)

@app.route('/')
def index():
    return ("WELCOME. You are here.")


#USER SECTION
users = []

class Users(object):
    @app.route('/register', methods=['POST'])
    def register(self):
        if not request.is_json:
            return (400,"request not json")
        else:
            pass

if __name__ == '__main__':
    app.run()