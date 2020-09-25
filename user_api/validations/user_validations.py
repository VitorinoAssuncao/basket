from user_api.models.user_models import User

def validate_login(value,flag):
    if isinstance(value,str) == False:
        return "Login digitado não é do tipo String."
    if flag  == "creation":
        if User.query.filter_by(user_login=value).first() != None:
            return "Login já cadastrado, por favor selecione outro."

    return True

def validate_name(value):
    if isinstance(value,str) == False:
        return "O nome digitado não é do tipo String."
    else:
        return True

def validate_password(value):
    if isinstance(value,str) == False:
        return "A senha digitada não é do tipo String."
    if len(value) < 8:
        return "A senha precisa ter no mínimo 8 digitos."
    return True

def validate_email(value):
    if isinstance(value,str) == False:
        return "O email digitado não é do tipo String."
    else:
        return True

def validate_user_data(data:dict, flag:str):
    result_login = validate_login(data['login'], flag)
    if result_login != True:
        return result_login

    result_name = validate_name(data['name'])
    if result_name != True:
        return result_name 
    if flag=="creation":
        result_password = validate_password(data['password'])
        if result_password != True:
            return result_password

    result_email = validate_email(data['email'])
    if result_email != True:
        return result_email

    return True           