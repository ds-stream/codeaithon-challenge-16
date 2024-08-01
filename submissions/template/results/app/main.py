from fastapi import FastAPI

from . import database

app = FastAPI()


@app.on_event("startup")
def on_startup():
    database.create_db_and_tables()
