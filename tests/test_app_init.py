import unittest

from unittest.mock import patch, MagicMock
from todo.config import _init_config_file, _create_databse

from todo import SUCCESS, DIR_ERROR
from pathlib import Path

test_db_path = Path.home().joinpath('.' + Path.home().stem + "._todo.json")

class TestAppInit(unittest.TestCase):
    
    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.touch')
    def test_init_config_file_success(self, mock_touch, mock_mkdir):
        mock_mkdir.return_value = None
        mock_touch.return_value = None
        
        result = _init_config_file()
        
        self.assertEqual(result, SUCCESS)
        
        mock_mkdir.assert_called_once_with(exist_ok=True)
        mock_touch.assert_called_once_with(exist_ok=True)
        
    @patch('pathlib.Path.mkdir')
    @patch('pathlib.Path.touch')
    def test_init_config_dir_error(self, mock_touch, mock_mkdir):
        mock_mkdir.side_effect = OSError
        
        result = _init_config_file()
        
        self.assertEqual(result, DIR_ERROR)
        
        mock_mkdir.assert_called_once_with(exist_ok=True)
        mock_touch.assert_not_called()