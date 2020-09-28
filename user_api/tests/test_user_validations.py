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