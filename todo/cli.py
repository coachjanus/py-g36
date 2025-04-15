from todo.ui import UI
import typer
from todo import config, ERRORS, db
from pathlib import Path

from typing import Annotated

import logging

logging.basicConfig(filename="todo.log", level=logging.INFO)

app = typer.Typer()

@app.command()
def init(
    # db_path = typer.Option(str(config.DEFAULT_DB_FILE_PATH), prompt="TODO database location?")):
    
    db_path: Annotated[str, typer.Option("--db-path", "-db", prompt="TODO database location?"), ] = str(config.DEFAULT_DB_FILE_PATH), ) -> None:
    
    app_init_error = config.init_app(db_path)
    
    if app_init_error:
        typer.secho(f"Crerating config file failed with {ERRORS[app_init_error]}", fg=typer.colors.RED)
        logging.error(f"Crerating config file failed with {ERRORS[app_init_error]}")
        raise typer.Exit(1)
    
    db_init_error = db.init_database(Path(db_path))
    if db_init_error:
        typer.secho(f"Crerating database failed with {ERRORS[db_init_error]}", fg=typer.colors.RED)
        logging.error(f"Crerating database failed with {ERRORS[db_init_error]}")
        raise typer.Exit(1)
    
    typer.secho(f"The todo database id {db_path}", fg=typer.colors.GREEN)
    logging.info(f"The todo database id {db_path}")


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
         

