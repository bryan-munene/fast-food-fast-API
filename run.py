from app import app
from flask import Flask, flash, redirect, render_template, request, session, jsonify, make_response
import os



app = Flask(__name__)

@app.route('/')
def index():
    return ("WELCOME. You are here.")



if __name__ == '__main__':
    app.run()