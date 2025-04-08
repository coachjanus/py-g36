from pathlib import Path
import json
from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

class DBHandler:
    def __init__(self, db_path:Path):
        self._db_path = db_path
        
    def write_todos(self, todo_list):
        pass
    
    def read_todos(self):
        pass
    