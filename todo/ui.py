from todo import __app_name__, __version__, config, db, ERRORS

from todo.tasks import TaskList

from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
import typer
from todo.task import Task

def make_title(fn):
    def wrapper():
        func = fn()
        output = func.title()
        return output
    return wrapper

@make_title
def to_upper():
    return f"Coose sone category"

class UI:
    
    keys = ['name', 'style', 'width', 'min_width', 'justify']
    
    values = [
        ["#", "dim", 6, None, "left"],
        ["Todo", None, None, 20, "left"],
        ["Category", None, None, 12, "right"],
        ["Done", None, None, 12, "right"],
    ]
    
    
    COLORS = {
        'LEARN': 'yellow',
        'WORK': 'red',
        'SPORT': 'cyan',
        'STUDY': 'green'
    }
    
    DONE = chr(9989)
    PENDING = chr(10060)
    
    # @classmethod
    def join_category(self):
        res = ""
        for k, v in UI.COLORS.items():
            res += f"[bold white on {v}] {k} [/]"
        return res
    
    @staticmethod
    def get_category_color(category):
        if category in UI.COLORS:
            return UI.COLORS[category]
        return "white"
    
    

    def choose_category(self):
        # return f"[bold green on blue]{to_upper()}: [/] {self.join_category()}"
        return Prompt.ask("[bold green on white] Coose some category: [/]" + self.join_category(), default="WORK")

    
    
    def __init__(self) -> None:
        # self.task_list = TaskList()
        self.task_list = self.get_tasks()
        self.console = Console()
        
    def get_tasks(self):
        if config.CONFIG_FILE_PATH.exists():
            db_path = db.get_database_path(config.CONFIG_FILE_PATH)
        else:
            typer.secho("Config file not found. Please run todo init", fg=typer.colors.RED)
            raise typer.Exit(1)
        if db_path.exists():
            return TaskList(db_path)
        else:
            typer.secho("Database not found. Please run todo init", fg=typer.colors.RED)
            raise typer.Exit(1)
    
    def help_me(self): 
        typer.secho("""
        All that You can do:
            l: Show all tasks
            a: Add new task
            u: Set done existing task
            d: Delete existing task
            h: Print this help
            q: Exit
        """, fg=typer.colors.RED)
    
    def bye(self):
        print(f"Thanks for using {__app_name__}.upper()")
    
    def hi(self):
        self.console.print(f"[bold magenta] Hi! It's me, {__app_name__.upper()} [/]", chr(128187), f"[bold magenta] {__version__}")
        # print(f"Hi! It's me, {__app_name__.upper()}")
    
    def your_choice(self):
        # return input(f"Please make Your choice (l|a|u|d|h|q) >>> ")
        return Prompt.ask(f"[bold yellow on blue] Please make Your choice (l|a|u|d|h|q) >>>  [/]")
    
    def prompt_for_lookup(self) -> str:
        return input("What You looking for? ")
    
    def add_your_task(self) -> str:
        return Prompt.ask("[bold green on blue] Text Your task [/]", default="Todo something else")

    def add_task(self):
                
        # description = input("Enter task description: ").strip().lower()
        description = self.add_your_task()
        # category = input("Enter task category: ").strip().upper()
        category = self.choose_category()
        current_todo = Task(description, category)
        current_todo, write_error = self.task_list.add(current_todo)
        
        if write_error:
            typer.secho(f"Added task failed with {write_error}", fg=typer.colors.RED)
            raise typer.Exit(1)
        typer.secho(f"Task {description} was added to todo database with {category}", fg=typer.colors.GREEN)
        
        # self.task_list.add(description, category)


   
    def all_task(self):
        tasks, error = self.task_list.get_tasks_list()
        if error:
            typer.secho(f"Fetching tasks failed with {ERRORS[error]}", fg=typer.colors.RED)
            raise typer.Exit(1)
        else:
            if len(tasks) == 0:
                typer.secho(f"There are no tasks in the todo list", fg=typer.colors.RED)
                raise typer.Exit(1)
            self.show(tasks)
            
    def make_header(self):
        headers = []
        for v in UI.values:
            d = dict(zip(UI.keys, v))
            headers.append(d)
        return headers
    
    
    def show(self, tasks):
        table = Table(show_header=True, header_style="bold blue")
        header = self.make_header()
        
        for item in header:
            table.add_column(item['name'], style=item['style'], width=item['width'], min_width=item['min_width'], justify=item['justify'])
        
        for index, task in enumerate(tasks, start=1):
            c = UI.get_category_color(task['_category'])
            is_done = UI.DONE if task['_status'] == True else UI.PENDING
            table.add_row(str(index), task['_description'], f"[{c}] {task['_category']} [/{c}]", is_done)
            
        self.console.print(table)
        
    def remove_task(self):
        contacts = get_all_contacts(db_name)
        name = prompt_for_lookup()
        contact = lookup_contact(contacts, name)
        
        confirm = input("Are You sure You want delete this contact? (y/n): ").strip()
        if confirm.lower() in ('yes', 'y'):
            return delete_contact(db_name, contacts, contact)
        return

    def lookup_task(self, name):
        first_name = ''
        last_name = ''
        
        words = name.split()
        
        if len(words) == 2:
            first_name, last_name = words
        elif len(words) == 1:
            first_name = words[0]
            
        for d in contacts:
            if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
                return d
            elif d['first_name'] == words[0].lower() or d['last_name'] == words[0].lower():
                return d
        
    def set_done_task(self):
        contacts = get_all_contacts(db_name)
        name = prompt_for_lookup()
        contact = lookup_contact(contacts, name)
        
        old_first_name = contact['first_name']
        old_last_name = contact['last_name']
        old_mobile = contact['mobile']
        
        first_name = input(f"Enter first name: ({old_first_name}) >>> ").strip().lower() or old_first_name
        last_name = input(f"Enter last name: ({old_last_name}) >>> ").strip().lower() or old_last_name
        mobile = input(f"Enter phone number: ({old_mobile}) >>> ").strip() or old_mobile
        
        update_contact(db_name, contacts, contact, {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'mobile': mobile})
    
