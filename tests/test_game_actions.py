import unittest
from unittest.mock import patch, Mock, MagicMock
from app.basketball_api.actions.game_actions import *
from app.basketball_api.models.game_models import *

class TestGameActions(unittest.TestCase):

    @patch('app.basketball_api.actions.game_actions.commit')
    @patch('app.basketball_api.actions.game_actions.save')
    # @patch('app.basketball_api.models.game_models.Game')
    def test_create_game(self, mock_save,mock_commit):
        """ verifica se o objeto foi criado corretamente"""
        game_data={
            'user_id':2222,
            'number':'12345678',
            'seasson':'testes',
            'points':2222
            }    
        
        mock_save.return_value=game_data
        mock_commit.return_value = mock_save
      
       
        result = create(game_data) 
       
        self.assertEqual(result['number'],game_data['number'])
        self.assertEqual(result['seasson'],game_data['seasson'])
        self.assertEqual(result['points'],game_data['points'])

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_game_by_id(self,queryMOCK):
        game_data={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
        #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = game_data

        mock_return = queryMOCK.query.filter_by.first
        result = get_game_by_id(1)
        self.assertEqual(result,game_data)
    
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_game_by_number(self,queryMOCK):
        game_data={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
     #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.first\
            .return_value = game_data

        mock_return = queryMOCK.query.filter_by.first
        result = get_game_by_number(1)
        self.assertEqual(result,game_data)  

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_all_games_by_user(self,queryMOCK):
        game_data={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
        #setup
        queryMOCK\
            .return_value.filter_by\
            .return_value.all\
            .return_value = game_data

        mock_return = queryMOCK.query.filter_by.first
        result = get_all_games_by_user(1)
        self.assertEqual(result,game_data)     

    @patch('app.basketball_api.actions.game_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.basketball_api.models.game_models.Game')
    def test_delete(self,mock_game,queryMOCK,mock_commit):
        #setup
        game_data ={
            'user_id':2222,
            'number':'12345678',
            'seasson':'testes',
            'points':2222
        }

        queryMOCK\
            .return_value.filter_by\
            .return_value.delete\
            .return_value = mock_game

        mock_commit.return_value =mock_game
        mock_return = queryMOCK.query.filter_by.delete
        result = delete_game(2)
        self.assertEqual(result,"Partida removida com sucesso.")  

    @patch('app.basketball_api.actions.game_actions.commit')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    @patch('app.basketball_api.models.game_models.Game')
    def test_update_game(self,mock_game,queryMOCK,mock_commit):
        #setup
        updated_game={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
        mock_game.return_value = {'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':55555
                                }
        queryMOCK\
            .return_value.query\
            .return_value = mock_game

        mock_commit.return_value =mock_game
        mock_return = queryMOCK.query.get
        result = update_game(2,updated_game)
        self.assertIsNotNone(result)           

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_all_games(self,queryMOCK):
        game_data = {
            'user_id':2222,
            'number':'12345678',
            'seasson':'testes',
            'points':2222
            }
        #setup
        queryMOCK\
            .return_value.query\
            .return_value.all\
            .return_value = game_data

        mock_return = queryMOCK.query.all
        result = get_all_games()
        self.assertIsNotNone(result)        

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_get_all_games_by_seasson(self,queryMOCK):
      
        all_games =[ {'game_id':1,
                    'game_user_id':2,
                    'game_number':1,
                    'game_seasson':23,
                    'game_points':555
                    },
                    {'game_id':2,
                    'game_user_id':2,
                    'game_number':2,
                    'game_seasson':23,
                    'game_points':444
                    },
                    {'game_id':3,
                    'game_user_id':2,
                    'game_number':3,
                    'game_seasson':23,
                    'game_points':666
                    }]
       
        queryMOCK\
        .return_value.query\
        .return_value.filter_by\
        .return_value.filter_by\
        .return_value.order_by\
        .return_value.all\
        .return_value = all_games 
        print(all_games)
        mock_return = queryMOCK.query.filter_by.order_by.all
        print(mock_return)
        result = get_all_games_by_seasson(2,23)
        self.assertEqual(result,[])      