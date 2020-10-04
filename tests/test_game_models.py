import unittest
from unittest.mock import patch, Mock, MagicMock
from app.basketball_api.models.game_models import *

class TestGameModel(unittest.TestCase):
    @patch('app.basketball_api.models.game_models.Game.serialize')    
    def test_game_creation(self,game):
        basket = {
            'user_id': 3,
            'number' : 4,
            'seasson':5,
            'points':8
        }
        game.return_value = basket
              
        retorno =Game( game_user_id=basket['user_id'],
                    game_number=basket['number'],
                    game_seasson=basket['seasson'],
                    game_points=basket['points'])
        retorno.serialize = basket              

        self.assertEqual(retorno.serialize,basket)    
      

