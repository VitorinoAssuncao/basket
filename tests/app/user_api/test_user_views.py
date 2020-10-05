import unittest
from flask import request
import flask
from unittest.mock import patch, Mock, MagicMock
from app.user_api.actions.user_actions import *
from app.user_api.models.user_models import *
from app.user_api.views.user_views import *
from main import app


class TestUserViews(unittest.TestCase):

    @patch('app.basketball_api.actions.game_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.basketball_api.views.game_views.update_game')
    def test_get_user_by_id(self, get_user_by_id, mock_sql, mock_commit):
       
        user = User(
                    user_login=1,
                    user_password='fgdrgdrg',
                    user_name='dfsdfsf',
                    user_email='grgdrgrdghyr')
        id = 'd4sa68das1'
        mock_sql.get.return_value = user
        mock_commit.return_value = Mock()
        get_user_by_id.return_value = user

        response = app.config.get(f'/users/{id}')
        result = get_user_by_id(1)
    
        self.assertIsNotNone(result)  