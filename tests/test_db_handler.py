import pytest
from todo.db_handler import DBHandler

from pathlib import Path

from unittest.mock import mock_open

test_db_path = Path.home().joinpath('.' + Path.home().stem + "._todo.json")

def test_read_todos_succes(mocker):
    mocker.patch('builtings.open', mock_open(read_data='''[{
        "description": "Todo something else",
        "category": "WORK",
        "status": True,
        "position": 1  
        }]'''))
    
    db_handler = DBHandler(Path(test_db_path))
    response = db_handler.read_todos()
    assert len(response.tasks_list) == 1
    assert response.tasks_list[0]['description'] == "Todo something else"
    assert response.tasks_list[0]['category'] == "WORK"
    