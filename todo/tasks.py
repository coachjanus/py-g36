
from todo.task import Task
from todo.db_handler import DBHandler
from todo import DB_READ_ERROR

class TaskList:
    
    def __init__(self, db_path) -> None:
        self._db_handler = DBHandler(db_path)
        
    # def get_todo_list(self):
    #     return self.todo_list
    
    def get_tasks_list(self):
        tasks_list, read_error = self._db_handler.read_todos()
        return (tasks_list, read_error)
    
    def add(self, task: Task):
        tasks_list, read_error = self._db_handler.read_todos()
        if read_error == DB_READ_ERROR:
            return (task, read_error)
        
        count = len(tasks_list)
        task._position = count if count else 0
        # task = Task(description, category)
        
        tasks_list.append(task)
        
        tasks_list, write_error =  self._db_handler.write_todos(tasks_list)
        return (task, write_error)
    
    def complete(self):
        pass