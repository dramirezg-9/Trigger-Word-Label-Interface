import os
from flask import g
from sqlmodel import create_engine, Session

# read this from your env (python-dotenv will load .env for you)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///app.db")
engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Session:
    if "db" not in g:
        g.db = Session(engine)
    return g.db

def close_session(e=None):
    db = g.pop("db", None)
    if db:
        db.close()