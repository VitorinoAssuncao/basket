import unittest
from unittest.mock import patch, Mock, MagicMock
from app.user_api.actions.user_actions import *
from app.user_api.models.user_models import User

class TestUserActions(unittest.TestCase):
    
    @patch('app.user_api.actions.user_actions.commit')
    @patch('app.user_api.actions.user_actions.save')
    @patch('app.user_api.actions.user_actions.generate_password_hash')
    def test_create_user(self, mock_hash,mock_save,mock_commit):
        """ verifica se o objeto foi criado corretamente"""
        mock_hash.return_value ='55555555555'
        
        dicionario_para_teste={'login':'testes',
                                'password':'12345678',
                                'name':'testes',
                                'email':'testes@gmail.com.br'
                                }
               
        mock_save.return_value=dicionario_para_teste
        mock_commit.return_value = mock_save
        resultado = create(dicionario_para_teste) 
       
        self.assertEqual(resultado['login'],dicionario_para_teste['login'])
        self.assertEqual(resultado['name'],dicionario_para_teste['name'])
        self.assertEqual(resultado['email'],dicionario_para_teste['email'])
    



    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_get_user_by_id_return_true(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = 1 #empty list of current product_id

        mock_return = queryMOCK.query.filter_by.first
        result = get_user_by_id(1)
        self.assertEqual(result,1)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_get_all(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.all\
            .return_value = [1,2,3] #empty list of current product_id

        mock_return = queryMOCK.query.all
        result = get_all_user()
        self.assertEqual(result,[1,2,3])

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.user_api.actions.user_actions.check_password_hash')
    @patch('app.user_api.models.user_models.User')
    def test_if_login_with_user_that_not_exist(self,mock_user,mock_hash,queryMOCK):
    #setup
        mock_user.return_value =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'testes',
                                    'email':'testes@gmail.com.br'
                                }
        mock_hash.return_value = True
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        mock_return = queryMOCK.query.filter_by.first
        result = login(1,'abcd')
        self.assertFalse(result)



    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.user_api.actions.user_actions.check_password_hash')
    @patch('app.user_api.models.user_models.User')
    def test_if_login_with_user_that_exist(self,mock_user,mock_hash,queryMOCK):
    #setup
        mock_user.return_value =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'testes',
                                    'email':'testes@gmail.com.br'
                                }
        mock_hash.return_value = True
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = mock_user

        mock_return = queryMOCK.query.filter_by.first
        result = login(2,'12345678')
        self.assertEqual(result.id,mock_user.id)
        
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.user_api.actions.user_actions.check_password_hash')
    @patch('app.user_api.models.user_models.User')
    def test_if_login_with_user_that_exist_333333(self,mock_user,mock_hash,queryMOCK):
    #setup
        mock_user.return_value =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'testes',
                                    'email':'testes@gmail.com.br'
                                }
        mock_hash.return_value = False
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = mock_user

        mock_return = queryMOCK.query.filter_by.first
        result = login(2,'12345678')
        self.assertEqual(result,False)     

    @patch('app.user_api.actions.user_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.user_api.models.user_models.User')
    def test_delete(self,mock_user,queryMOCK,mock_commit):
    #setup
        mock_user.return_value =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'testes',
                                    'email':'testes@gmail.com.br'}
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = mock_user

        mock_commit.return_value =mock_user
        mock_return = queryMOCK.query.filter_by.first
        result = delete_user(2)
        self.assertEqual(result,"Usuário removido com sucesso.")  

    @patch('app.user_api.actions.user_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.user_api.models.user_models.User')
    def test_update(self,mock_user,queryMOCK,mock_commit):
    #setup
        dicionari_atualizado =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'atualizar',
                                    'email':'testes@gmail.com.br'}
        mock_user.return_value =  {'id':2,
                                    'login':'testes',
                                    'password':'12345678',
                                    'name':'testes',
                                    'email':'testes@gmail.com.br'}
        queryMOCK\
            .return_value.query\
            .return_value = mock_user

        mock_commit.return_value =mock_user
        mock_return = queryMOCK.query.get
        result = update_user(2,dicionari_atualizado)
        self.assertIsNotNone(result)            