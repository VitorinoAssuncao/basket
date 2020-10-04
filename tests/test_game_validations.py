import unittest
from unittest.mock import patch, Mock, MagicMock
from app.basketball_api.actions.game_actions import *
from app.basketball_api.models.game_models import *
from app.basketball_api.validations.game_validations import *

class TesteGameValidations(unittest.TestCase):

    def test_validate_game_number_is_not_int(self):
        retorno = validate_game_number_is_int('teste')
        self.assertEqual(retorno,"Este jogo já foi lançado para essa temporada." )
    
    def test_validate_game_number_is_int_is_true(self):
        dicionario_para_teste={'user_id':9,
                                'number':7,
                                'seasson':7,
                                'points':34
                                }
        retorno = validate_game_number_is_int(dicionario_para_teste['seasson'])
        self.assertEqual(retorno,True)   

    def test_validate_seasson_is_int(self):
        retorno = validate_seasson_is_int('teste')
        self.assertEqual(retorno,"O campo 'Temporada' não recebeu um valor inteiro."  )

    def test_validate_seasson_is_int_is_true(self):
        retorno = validate_seasson_is_int(1)
        self.assertEqual(retorno,True)   


    def test_validate_points_is_int(self):
        retorno = validate_points_is_int('teste')
        self.assertEqual(retorno,"O campo 'Pontos' não recebeu um valor inteiro." )

    def test_validate_points_is_int_is_true(self):
        retorno = validate_points_is_int(1)
        self.assertEqual(retorno,True) 
  
    @patch('app.basketball_api.validations.game_validations.validate_user_id_is_int')    
    @patch('app.basketball_api.validations.game_validations.validate_user_id_exist')     
    @patch('app.basketball_api.validations.game_validations.validate_seasson_is_int') 
    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_int') 
    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_not_repeated')     
    def test_points_is_int(self,
                                   mock_validate_game_number_is_not_repeated,
                                   mock_validate_game_number_is_int,
                                   mock_validate_seasson_is_int,
                                   mock_validate_user_id_exist,
                                   mock_validate_user_id_is_int ):

        dicionario_para_teste={'user_id':9,
                                'number':7,
                                'seasson':7,
                                'points':34
                                }
        
        mock_validate_game_number_is_not_repeated.return_value = True
        mock_validate_game_number_is_int.return_value = True
        mock_validate_seasson_is_int.return_value = True
        mock_validate_user_id_exist.return_value = True
        mock_validate_user_id_is_int.return_value = True

                              
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno,True)       

    @patch('app.basketball_api.validations.game_validations.validate_user_id_is_int')    
    @patch('app.basketball_api.validations.game_validations.validate_user_id_exist')     
    @patch('app.basketball_api.validations.game_validations.validate_seasson_is_int') 
    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_int') 
    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_not_repeated')     
    def test_points_is_not_int(self,
                                   mock_validate_game_number_is_not_repeated,
                                   mock_validate_game_number_is_int,
                                   mock_validate_seasson_is_int,
                                   mock_validate_user_id_exist,
                                   mock_validate_user_id_is_int ):

        dicionario_para_teste={'user_id':9,
                                'number':7,
                                'seasson':7,
                                'points':'34'
                                }
        
        mock_validate_game_number_is_not_repeated.return_value = True
        mock_validate_game_number_is_int.return_value = True
        mock_validate_seasson_is_int.return_value = True
        mock_validate_user_id_exist.return_value = True
        mock_validate_user_id_is_int.return_value = True

                              
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno,"O campo 'Pontos' não recebeu um valor inteiro.")       
    

    def test_validate_points_is_int_is_2000(self):
        retorno = validate_points_is_int(2000)
        self.assertEqual(retorno,"O valor máximo do campo 'Pontos' é de 1000." )  



    def test_validate_game_data(self):
        dicionario_para_teste={'user_id':'2222',
                                'number':'12345678',
                                'seasson':'testes',
                                'points':'2222'
                                }
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno,"O campo 'Código de Usuário' não recebeu um valor inteiro.")

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_validate_game_data_if_user_id_is_int(self,queryMOCK):
        dicionario_para_teste={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
        queryMOCK\
        .return_value.filter_by\
        .return_value.first\
        .return_value = None

        mock_return = queryMOCK.query.filter_by.first
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno,'O usuário informado não existe, favor verificar.')   

    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_validate_game_data_if_user_id_is_not_int(self,queryMOCK):
        dicionario_para_teste={'user_id':2222,
                                'number':'12345678',
                                'seasson':'testes',
                                'points':2222
                                }
        queryMOCK\
        .return_value.filter_by\
        .return_value.first\
        .return_value = dicionario_para_teste

        mock_return = queryMOCK.query.filter_by.first
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno,"O campo 'Temporada' não recebeu um valor inteiro.") 

    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_int')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_validate_game_number_is_repeated(self,queryMOCK,mock_int):
        dicionario_para_teste={'user_id':2222,
                                    'number':2222,
                                    'seasson':2222,
                                    'points':2222
                                    }
        queryMOCK\
        .return_value.filter_by\
        .return_value.first\
        .return_value = dicionario_para_teste 
        mock_int.return_value = True                        
        retorno = validate_game_data(dicionario_para_teste)
        self.assertEqual(retorno, 'Este jogo já foi lançado para essa temporada.')    
   

    @patch('app.basketball_api.validations.game_validations.validate_game_number_is_int')
    @patch("flask_sqlalchemy._QueryProperty.__get__")
    def test_validate_game_number_is_not_repeated(self,queryMOCK,mock_int):
        dicionario_para_teste={'user_id':678787,
                                    'number':8989,
                                    'seasson':676,
                                    'points':76567
                                    }
        queryMOCK\
        .return_value.filter_by\
        .return_value.first\
        .return_value = None   
        mock_int.return_value = True                   
        retorno = validate_game_number_is_not_repeated(dicionario_para_teste['number'],
                                                        dicionario_para_teste['user_id'],
                                                        dicionario_para_teste['seasson'])
        self.assertEqual(retorno,True)                                       