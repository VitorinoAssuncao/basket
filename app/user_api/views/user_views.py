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

from app.user_api.actions.user_actions import create
from app.user_api.actions.user_actions import login
from app.user_api.actions.user_actions import get_user_by_id
from app.user_api.actions.user_actions import get_all_user
from app.user_api.actions.user_actions import update_user
from app.user_api.actions.user_actions import delete_user
from app.user_api.validations.user_validations import validate_user_data

app_user = Blueprint("app_user",__name__)

@app_user.route("/",methods=["GET","POST"])
def login_user():

    session['user_id'] = None       #Limpa a varíavel de sessão ao carregar a pagina, para que funcione como logoff
    error = " "                     # Varíavel para armazenar o erro

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

    return redirect("/users/"+str(session.get('user_id')))

@app_user.route("/users/registry",methods=["GET","POST"])
def post():
    error = " "
    result = None

    if request.method == 'POST' :
        user_data = {
            'login': request.form['username'],
            'password': request.form['password'],
            'name': request.form['fullname'],
            'email': request.form['email']
        }
        result = validate_user_data(user_data,"creation") 
        if result != True:
            error = result
            return render_template("user_register.html",error=error)
        else:            
            user = create(user_data)
            user_data = user.serialize()
    else:
        return render_template("user_register.html")

    session['user_id'] = user_data['id']
    return render_template("user_page.html",user=user_data)

@app_user.route("/users/<id>",methods=["GET"])
def get_user(id:int):
    user = get_user_by_id(id)
    user_data = user.serialize()
    return render_template("user_page.html",user=user_data)

@app_user.route("/users/<user_id>",methods=["POST"])
def update(user_id:int):
    update_data = {
        'login': request.form['username'],
        'name': request.form['fullname'],
        'email': request.form['email']
    }
    result = validate_user_data(update_data,"update")
    if result == True:
        updated_user = update_user(user_id,update_data)
        user_data = updated_user.serialize()
        return render_template("user_page.html",user=user_data)
    else:
        return render_template("user_page.html",error=result)

#  Neste pedaço estão colocadas rotas inativadas, para possível uso futuro 

# @app_user.route("/users",methods=["GET"])
# def get_all():
#     return jsonify([user.serialize() for user in get_all_user()])

# @app_user.route("/users/<user_id>",methods=["DELETE"])
# def delete(user_id:int):
#     result =  delete_user(user_id)
#     return result,200