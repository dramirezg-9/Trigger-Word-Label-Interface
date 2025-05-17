from flask import Flask
from .db import close_session     # import from db, not routes
from .routes import bp as main_bp

def create_app(config_object: str = "config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_object)

    # register teardown so sessions close after each request
    app.teardown_appcontext(close_session)

    # register blueprints
    app.register_blueprint(main_bp)

    return app