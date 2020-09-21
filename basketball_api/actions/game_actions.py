from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from basketball_api.models.game_models import Game

from database.database import save
from database.database import commit
from database.database import db

def create(data:dict) -> Game:
    return save(
        Game(
            game_user_id = data['user_id'],
            game_number = data['number'],
            game_seasson = data['seasson'],
            game_points = data['points']
        )
    )

def get_game_by_id(id:int) -> Game:
    game = Game.query.filter_by(game_id=id).first()
    return game

def get_game_by_number(number:int) -> Game:
    game = Game.query.filter_by(game_number=number).first()
    return game

def get_all_games() -> dict:
    all_games = Game.query.all()
    return all_games

def get_all_games_by_user(user_id:int) -> dict:
    all_games = Game.query.filter_by(game_user_id = user_id).all()
    return all_games

def get_all_games_by_seasson(seasson:int, user_id:int) -> dict:
    all_games = Game.query.filter_by(game_seasson = seasson,game_user_id = user_id).all()
    return all_games


def update_game(game_id:int,data_to_update:dict) -> Game:
    game_updated = Game.query.get(game_id)
    game_updated.game_number = data_to_update['number']
    game_updated.game_seasson = data_to_update['seasson']
    game_updated.game_points = data_to_update['points']
    commit()
    return game_updated

def delete_game(id:int) -> str:
    Game.query.filter_by(game_id=id).delete()
    commit()
    return "Partida removida com sucesso." 