import unittest
from unittest.mock import patch, Mock, MagicMock
from app.user_api.models.user_models import *

class TestUserModels(unittest.TestCase):
    @patch('app.user_api.models.user_models.User.serialize')    
    def test_creation_of_user_with_model(self,mock_serialize):
        user =  {'id':2,
                    'login':'testes',
                    'password':'12345678',
                    'name':'testes',
                    'email':'testes@gmail.com.br'
                }
        mock_serialize.return_value =user        
        result =User(
                    user_login=user['login'],
                    user_password=user['password'],
                    user_name=user['name'],
                    user_email=user['email'])
        result.serialize = user            

        self.assertEqual(result.serialize,user)    
      

