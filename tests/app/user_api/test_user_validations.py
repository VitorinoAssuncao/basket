import unittest
from unittest.mock import patch, Mock, MagicMock
from app.user_api.validations.user_validations import *
from app.user_api.models.user_models import User



class TestUserValidations(unittest.TestCase):
    
    def test_if_validate_name_return_true(self):
        result = validate_name('joao')
        self.assertTrue(result)

    def test_if_validate_name_return_message_when_value_int_is_used(self):
        result = validate_name(1234)
        self.assertEqual(result,"O nome digitado não é do tipo String.")

    def test_if_validate_password_return_true(self):
        result = validate_password("123456789")
        self.assertTrue(result)
    
    def test_if_validate_password_return_message_when_value_not_str_is_used(self):
        result = validate_password(123456789)
        self.assertEqual(result,"A senha digitada não é do tipo String.")

    def test_if_validate_password_return_message_when_psw_length_less_than_eight(self):
        result = validate_password("abc")
        self.assertEqual(result,"A senha precisa ter no mínimo 8 digitos.")

    def test_if_validate_email_return_true(self):
        result = validate_email("joao@gmail.com")
        self.assertTrue(result)

    def test_if_validate_email_return_message_when_value_not_str_is_used(self):
        result = validate_email(123456)
        self.assertEqual(result,"O email digitado não é do tipo String.")

    def test_if_validate_login_return_message_when_value_not_str_is_used(self):
        result = validate_login(123456,"login")
        self.assertEqual(result,"Login digitado não é do tipo String.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_login_in_creation_return_true(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        mock_return = queryMOCK.query.filter_by.first
        result = validate_login("joao","creation")
        self.assertTrue(result)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_login_in_creation_return_message(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = 1 #empty list of current product_id

        mock_return = queryMOCK.query.filter_by.first
        result = validate_login("joao","creation")
        self.assertEqual(result,"Login já cadastrado, por favor selecione outro.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_validate_data_return_true(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        user_data = {
            'login': 'joao',
            'password': '123456789',
            'name': 'joao da silva',
            'email': 'joao@gmail.com'
        }
        
        result = validate_user_data(user_data,'update')

        self.assertTrue(result)

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_validate_data_msg_error_in_login(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        user_data = {
            'login': 123456,
            'password': '123456789',
            'name': 'joao da silva',
            'email': 'joao@gmail.com'
        }
        
        result = validate_user_data(user_data,'update')

        self.assertEqual(result,"Login digitado não é do tipo String.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_validate_data_msg_error_in_name(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        user_data = {
            'login': '123456',
            'password': '123456789',
            'name': 123456,
            'email': '124323'
        }
        
        result = validate_user_data(user_data,'update')

        self.assertEqual(result,"O nome digitado não é do tipo String.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_validate_data_msg_error_in_password(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        user_data = {
            'login': '123456',
            'password': '12345',
            'name': 'joao da silva',
            'email': '124323'
        }
        
        result = validate_user_data(user_data,'creation')

        self.assertEqual(result,"A senha precisa ter no mínimo 8 digitos.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_if_validate_data_msg_error_in_email(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        user_data = {
            'login': '123456',
            'password': '123456789',
            'name': 'joao da silva',
            'email': 124323
        }
        
        result = validate_user_data(user_data,'update')

        self.assertEqual(result,"O email digitado não é do tipo String.")

