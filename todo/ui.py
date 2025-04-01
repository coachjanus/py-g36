from todo import __app_name__

from todo.tasks import TaskList

from rich.table import Table
from rich.console import Console

class UI:
    
    keys = ['name', 'style', 'width', 'min_width', 'justify']
    
    values = [
        ["#", "dim", 6, None, "left"],
        ["Todo", None, None, 20, "left"],
        ["Category", None, None, 12, "right"],
        ["Done", None, None, 12, "right"],
    ]
    
    def __init__(self):
        self.task_list = TaskList()
        self.console = Console()
    
    def help_me(self):
        print("""
        All that You can do:
            l: Show all tasks
            a: Add new task
            u: Set done existing task
            d: Delete existing task
            h: Print this help
            q: Exit
        """)
    
    def bye(self):
        print(f"Thanks for using {__app_name__}.upper()")
    
    def hi(self):
        print(f"Hi! It's me, {__app_name__.upper()}")
    
    def your_choice(self):
        return input(f"Please make Your choice (l|a|u|d|h|q) >>> ")

    def prompt_for_lookup(self):
        return input("What You looking for? ")

    def add_task(self):
                
        description = input("Enter task description: ").strip().lower()
        category = input("Enter task category: ").strip().upper()
        self.task_list.add(description, category)


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
    
    def all_task(self):
        tasks = self.task_list.get_todo_list()
        if len(tasks) > 0:
            print(tasks)
            self.show(tasks)
        else:
            print("Your tasl list is empty. Go back to menu and add new task.")
            
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
            
        self.console.print(table)
        
