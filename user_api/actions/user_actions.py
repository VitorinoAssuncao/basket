from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from user_api.models.user_models import User

from database.database import save
from database.database import commit
from database.database import db

def create(data:dict) -> User:
""" Função responsável por receber um dicíonario com os dados do usuário, e criar seu usuário no banco.
    O campo password irá passar por um processo de hash, o gravando de forma mais segura no banco dessa forma.
"""
    return save(
        User(
            user_login = data['login'],
            user_password = generate_password_hash(data['password']),
            user_name = data['name'],
            user_email = data['email']
        )
    )

def get_user_by_id(user_id:int) -> User:
""" Função responsável por receber um id de usuário (código único, inteiro) e retornar os dados específicos do usuário
    Ex. get_user_by_id(1)
"""
    user = User.query.filter_by(user_id=user_id).first()
    return user

def get_all_user() -> dict:
""" Função responsável por pesquisar e retornar todos os usuários atualmente no sistema em formato de dicionario.
"""
    all_user = User.query.all()
    return all_user

def update_user(user_id:int,data_to_update:dict) -> User:
""" Função responsável pela atualização dos dados do usuário, recebendo o id do usuário que deverá ser alterado (user_id) e os dados de sua conta, observar que ele não inclui alterações no password.
    Ao final retorna um objeto do tipo Usuário.
"""    
    user_updated = User.query.get(user_id)
    user_updated.user_login = data_to_update['login']
    user_updated.user_name = data_to_update['name']
    user_updated.user_email = data_to_update['email']
    commit()
    return user_updated

def delete_user(id:int) -> str:
""" Função responsável pela exclusão de um usuário do banco, conforme o id de usuário informado (id)
"""
    User.query.filter_by(user_id=id).delete()
    commit()
    return "Usuário removido com sucesso." 

def login(login_data:str,password:str) -> User:
""" Função responsável pelo login do usuário, recebendo o login e senha digitados (login_data e password respectivamente), e primeiro verificando se o usuário existe, e em caso positivo, testando se essa senha é a do mesmo.
    Ex. login("dev","dev12345")
"""   
    user = User.query.filter_by(user_login=login_data).first()
    if user != None:
        if check_password_hash(user.user_password,password):
            return user
    else:
        return False

