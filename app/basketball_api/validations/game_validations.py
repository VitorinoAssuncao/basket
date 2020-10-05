from app.basketball_api.models.game_models import Game
from app.user_api.models.user_models import User

def validate_game_number_is_int(game_number):
    if isinstance(game_number,int) != True:
        return "O campo 'Partida' não recebeu um valor do tipo inteiro."
    else:
        return True

def validate_game_number_is_not_repeated(number=int,user_id=int,seasson=int):
    if Game.query.filter_by(game_user_id = user_id,game_number=number,game_seasson=seasson).first() != None:
        return "Este jogo já foi lançado para essa temporada."
    else: 
        return True

def validate_user_id_is_int(user_id):
    if isinstance(user_id,int) != True:
        return "O campo 'Código de Usuário' não recebeu um valor inteiro."
    else:
        return True

def validate_user_id_exist(id):
    if User.query.filter_by(user_id=id).first() == None:
        return "O usuário informado não existe, favor verificar."
    else:
        return True

def validate_seasson_is_int(seasson):
    if isinstance(seasson,int) != True:
        return "O campo 'Temporada' não recebeu um valor inteiro."
    else:
        return True

def validate_points_is_int(points):
    if isinstance(points,int) != True:
        return "O campo 'Pontos' não recebeu um valor inteiro."
    else:
        if points > 1000:
            return "O valor máximo do campo 'Pontos' é de 1000."
    
    return True
def validate_game_data(game_data:dict):
    result_user_id = validate_user_id_is_int(game_data['user_id'])
    if result_user_id != True:
        return result_user_id

    result_exist_user_id = validate_user_id_exist(game_data['user_id'])
    if result_exist_user_id != True:
        return result_exist_user_id

    result_seasson = validate_seasson_is_int(game_data['seasson'])
    if result_seasson != True:
        return result_seasson

    result_number = validate_game_number_is_int(game_data['number'])
    if result_number != True:
        return result_number

    result_number_repeat = validate_game_number_is_not_repeated(game_data['number'],game_data['user_id'],game_data['seasson'])
    if result_number_repeat != True:
        return result_number_repeat

    result_points = validate_points_is_int(game_data['points'])
    if result_points != True:
        return result_points

    return True