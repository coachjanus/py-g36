
from todo.task import Task
from todo.db_handler import DBHandler
from todo import DB_READ_ERROR
from todo.responses import TodoResponse, DBResponse


class TaskList:
    
    def __init__(self, db_path) -> None:
        self._db_handler = DBHandler(db_path)
    
    def get_tasks_list(self) -> DBResponse:
        reader = self._db_handler.read_todos()
        return DBResponse(reader.tasks_list, reader.error)
    
    def add(self, task: Task) -> TodoResponse:
        # tasks_list, read_error = self._db_handler.read_todos()
        
        reader = self._db_handler.read_todos()
        
        if reader.error == DB_READ_ERROR:
            return TodoResponse(task, reader.error)
        
        count = len(reader.tasks_list)
        task._position = count if count else 0
        
        reader.tasks_list.append(task)
        
        writer =  self._db_handler.write_todos(reader.tasks_list)
        return TodoResponse(task, writer.error)
    
    def complete(self):
        pass