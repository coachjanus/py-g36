
from todo.task import Task

class TaskList:
    
    def __init__(self):
        self.todo_list = []
        
    def get_todo_list(self):
        return self.todo_list
    
    def add(self, description, category):
        count = len(self.todo_list)
        task = Task(description, category)
        task._position = count if count else 0
        self.todo_list.append(task)
    
    def complete(self):
        pass