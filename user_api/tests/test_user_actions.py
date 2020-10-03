import unittest
from unittest.mock import patch, Mock, MagicMock
from user_api.actions.user_actions import *
from user_api.models.user_models import User

class TestUserActions(unittest.TestCase):

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
    def test_if_login_with_user_that_not_exist(self,queryMOCK):
    #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = None #empty list of current product_id

        mock_return = queryMOCK.query.filter_by.first
        result = login(1,'abcd')
        self.assertFalse(result)