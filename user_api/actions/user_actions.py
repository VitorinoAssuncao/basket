from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from user_api.models.user_models import User

from database.database import save
from database.database import commit
from database.database import db

def create(data:dict) -> User:
    return save(
        User(
            user_login = data['login'],
            user_password = generate_password_hash(data['password']),
            user_name = data['name'],
            user_email = data['email']
        )
    )

def get_user_by_id(user_id:int) -> User:
    user = User.query.filter_by(user_id=user_id).first()
    return user

def get_all_user() -> dict:
    all_user = User.query.all()
    return all_user

def update_user(user_id:int,data_to_update:dict) -> User:
    user_updated = User.query.get(user_id)
    user_updated.user_login = data_to_update['login']
    user_updated.user_password = generate_password_hash(data_to_update['password'])
    user_updated.user_name = data_to_update['name']
    user_updated.user_email = data_to_update['email']
    commit()
    return user_updated

def delete_user(user_id:int) -> str:
    User.query.filter_by(id=user_id).delete()
    commit()
    return "Usuário removido com sucesso." 

def login(login_data:str,password:str) -> User:
    user = User.query.filter_by(user_login=login_data).first()
    if check_password_hash(user.user_password,password):
        return user
    else:
        return False

