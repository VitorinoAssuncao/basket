import unittest
from unittest.mock import patch, Mock, MagicMock
from user_api.validations.user_validations import *

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
        result = validate(123456789)
        self.assertEqual(result,"A senha digitada não é do tipo String.")

    def test_if_validate_password_return_message_when_psw_length_less_than_eight(self):
        result = validate("abc")
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