from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from settings import DEBUG
from settings import HOST
from settings import PORT

from user_api.actions.user_actions import create
from user_api.actions.user_actions import login
from user_api.actions.user_actions import get_user_by_id
from user_api.actions.user_actions import get_all_user
from user_api.actions.user_actions import update_user
from user_api.actions.user_actions import delete_user
from user_api.validations.user_validations import validate_user_data

app_user = Blueprint("app_user",__name__)

@app_user.route("/users",methods=["GET","POST"])
def post():
    error = " "
    result = False
    if request.method == 'POST':
        user_data = {
            'login': request.form['username'],
            'password': request.form['password'],
            'name': request.form['fullname'],
            'email': request.form['email']
        }
        print(user_data)
        result = validate_user_data(user_data,"creation") 
        if result != True:
            error = result
            return render_template("register.html",error=error)
        else:            
            print(result)
            user = create(user_data)
            user_data = user.serialize()
    else:
        return render_template("register.html")
    return render_template("user_page.html",user=user_data)

@app_user.route("/users/login",methods=["GET","POST"])
def login_user():
    error = " "
    login_result = False
    if request.method == 'POST':
        login_data = {
            'login': request.form['username'],
            'password': request.form['password']
        }
        login_result = login(login_data['login'],login_data['password'])
        if login_result == False:
            error = "Login ou senha incorretos."
            return render_template("main.html", error=error)
        else:
             session['user_id'] = login_result.user_id
    else:
        return render_template("main.html")    
    return render_template("user_page.html")

@app_user.route("/users/<id>",methods=["GET"])
def get_user(id:int):
    user = get_user_by_id(id)
    return jsonify(user.serialize()),200

@app_user.route("/users",methods=["GET"])
def get_all():
    return jsonify([user.serialize() for user in get_all_user()])

@app_user.route("/users/<user_id>",methods=["PUT"])
def update(user_id:int):
    update_data = request.get_json()
    result = validate_user_data(update_data,"update")
    if result == True:
        updated_user = update_user(user_id,update_data)
        return jsonify(updated_user.serialize())
    else:
        return result

@app_user.route("/users/<user_id>",methods=["DELETE"])
def delete(user_id:int):
    result =  delete_user(user_id)
    return result,200