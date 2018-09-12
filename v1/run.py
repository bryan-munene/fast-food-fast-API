from app import app
from flask import Flask, flash, redirect, render_template, request, session, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import os



app = Flask(__name__)

@app.route("/")
def index():
    return "WELCOME. You are here."


#USER SECTION
users = []

class Users(object):
    @app.route("/register", methods=["POST"])
    def register():
        if not request.is_json:
            return jsonify(400,"request not json")
        else:
            data = request.get_json() 
            user_id =  len(users)+1
            name = data['name']
            email = data['email']
            username = data['username']
            password = data['password']
            password2 = data['password2']

        
        if not password == password2:
            return jsonify(403,"passwords don't match")

        
        if len(users) > 0:
            for user in users:
                e = user.get('email')
                u = user.get('username')
                p = user.get('password')
                
        else:
            user = {
                 "user_id":user_id,
                 "name":name,
                 "email":email,   
                 "username":username,
                 "password":password,
                 "admin":False
                 }

            users.append(user)

            return make_response(jsonify({"status":"created", "user":user, "users":users }),201)
                
                
        if email == e:
            return jsonify(403,"user already exists")
                    
        elif username == u and password == p:
            return jsonify(403,"user already exists")
                    
        else:
            user = {
                 "user_id":user_id,
                 "name":name,
                 "email":email,   
                 "username":username,
                 "password":password,
                 "admin":False
                 }

            users.append(user)

            return make_response(jsonify({"status":"created", "user":user, "users":users }),201)



    @app.route("/login")
    def home():
        if session.get('logged_in'):
            return make_response(jsonify({"status":"user logged in", "id":session['user_id'], "login":True}, ),200)
        elif session.get('logged_in_admin'):
            return make_response(jsonify({"status":"admin logged in", "login":True}, ),200)
        else:
            return make_response(jsonify({"status":"login error", "login":False}),401)
     
    @app.route("/login", methods=["POST"])
    def do_user_login():
        data = request.get_json()
        username = data['username']
        password = data['password']

        for user in users:
            u = user.get('username')
            p = user.get('password')
            r = user.get('admin')

            if password == p and username == u and r == False:
                session['user_id'] = user['user_id']
                session['logged_in'] = True
            elif password == p and username == u and r == True:
                session['logged_in_admin'] = True
            else:
                session['logged_in'] = False
                session['logged_in_admin'] = False
            
        return Users.home()

    



    @app.route("/logout")
    def logout():
        session['logged_in'] = False
        return Users.home()




if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)