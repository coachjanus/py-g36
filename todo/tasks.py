
from todo.task import Task
from todo.db_handler import DBHandler

class TaskList:
    
    def __init__(self, db_path):
        # self.todo_list = []
        self._db_handler = DBHandler(db_path)
        
    def get_todo_list(self):
        return self.todo_list
    
    def get_tasks_list(self):
        todo_list, read_error = self._db_handler.read_todos()
        return (todo_list, read_error)
    
    def add(self, description, category):
        count = len(self.todo_list)
        task = Task(description, category)
        task._position = count if count else 0
        self.todo_list.append(task)
    
    def complete(self):
        pass