from flask import Blueprint, render_template
from sqlmodel import select
from .models import User
# import session functions from db.py, not from app/__init__.py
from .db import get_session

bp = Blueprint("main", __name__)

@bp.route("/users")
def list_users():
    db = get_session()
    users = db.exec(select(User)).all()
    return render_template("users.html", users=users)
