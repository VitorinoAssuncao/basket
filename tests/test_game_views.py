import unittest
import flask
from unittest.mock import patch, Mock, MagicMock
from app.basketball_api.actions.game_actions import *
from app.basketball_api.models.game_models import *
from app.basketball_api.views.game_views import *

class TestGameViews(unittest.TestCase):
    @patch('app.basketball_api.validations.game_validations.validate_game_data') 
    @patch.object(flask,'request')
    @patch.object(flask,'session')
    def test_create_new_game(self,mock_session, mock_request,mock_validate_game_data):
        mock_session.get = 1
        mock_request.method = 'POST'
        mock_validate_game_data.return_value =False
       
        # Action
        response = app_game.post('/games',{})
        # data = response.get_json()
        self.assertEqual(response.status_code, 200) 

    

    @patch('app.basketball_api.actions.game_actions.update_game')
    def test_update_game(self, logs_mock):
        logs_mock.return_value = True
        with app_game.test_client() as c:
            response = c.put(f'/games{1}')
            contacts()
            teste, teste2 = update_game(Mock())
            flask.render_template = Mock()
            flask.render_template.return_value = Mock()
          
            self.assertEqual(response.status_code, 200)     