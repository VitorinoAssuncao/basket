
import unittest
from flask import request
import flask
from unittest.mock import patch, Mock, MagicMock
from app.basketball_api.actions.game_actions import *
from app.basketball_api.models.game_models import *
from app.basketball_api.views.game_views import *
from main import app


class TestGameViews(unittest.TestCase):

    @patch('app.basketball_api.actions.game_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.basketball_api.views.game_views.update_game')
    def test_get_by_id_should_return_category_with_the_same_id(self, get_category_by_id_mock, mock_sql, mock_commit):
       
        game = Game(game_id=1,
                    game_user_id=2,
                    game_number=1,
                    game_seasson=23,
                    game_points=555)
        id = 'd4sa68das1'
        mock_sql.get.return_value = game
        mock_commit.return_value = Mock()
        get_category_by_id_mock.return_value = game

        response = app.config.get(f'/games/{id}')
        result = update_game(1,game.serialize())
    
        self.assertIsNotNone(result)  