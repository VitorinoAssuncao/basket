from flask import Blueprint
from flask import jsonify
from flask import request
from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for

from settings import DEBUG
from settings import HOST
from settings import PORT

from basketball_api.actions.game_actions import create
from basketball_api.actions.game_actions import get_game_by_id
from basketball_api.actions.game_actions import get_all_games_by_user
from basketball_api.actions.game_actions import get_all_games_by_seasson
from basketball_api.actions.game_actions import get_all_games
from basketball_api.actions.game_actions import update_game
from basketball_api.actions.game_actions import delete_game
#from basketball_api.validations.user_validations import validate_user_data

app_game = Blueprint("app_game",__name__)

@app_game.route("/games",methods=["GET","POST"])
def post():
    error = ''
    if request.method == 'POST':
        game_data = {
        'user_id': session.get('user_id'),
        'number': request.form['game'],
        'seasson': request.form['seasson'],
        'points': request.form['points']
        }
        game = create(game_data)
        return jsonify(game.serialize()),201
    else:
        return render_template('games.html')

@app_game.route("/games/<id>",methods=["GET"])
def get_game(id:int):
    game = get_game_by_id(id)
    return jsonify(game.serialize()),200

@app_game.route("/games/all",methods=["GET"])
def get_all():
    return jsonify([game.serialize() for game in get_all_games()])

@app_game.route("/games_user/<id>",methods=["GET"])
def get_all_games_from_user(id:int):
    games = get_all_games_by_user(id)
    return jsonify([game.serialize() for game in games])

@app_game.route("/games_user/<id>&<seasson>",methods=["GET"])
def get_all_games_from_user_and_seasson(id:int,seasson:int):
    games = get_all_games_by_seasson(id,seasson)
    return render_template("game_info.html",games_data=games)

@app_game.route("/games/<id>",methods=["PUT"])
def update(id:int):
    update_data = request.get_json()
    result = True#validate_user_data(update_data,"update")
    if result == True:
        updated_game = update_game(id,update_data)
        return jsonify(updated_game.serialize())
    else:
        return result

@app_game.route("/games/<id>",methods=["DELETE"])
def delete(id:int):
    result =  delete_game(id)
    return result,200