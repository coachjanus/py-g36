from todo.ui import UI
import typer

app = typer.Typer()

@app.command()
def run():
    ui = UI()
    
    ui.hi()
    
    while True:
        match ui.your_choice():
            case 'a':
                ui.add_task()
            case 'l':
                ui.all_task()
            case 'u':
                ui.set_done_task()
            case 'd':
                ui.remove_task()
                
            case 'h':
                ui.help_me()
            case 'q':
                ui.bye()
                break
            case _:
                ui.help_me()
         

