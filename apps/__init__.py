from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db:SQLAlchemy = SQLAlchemy()
migrate = Migrate()

def create_app():   
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from apps.users import users as ubp
    app.register_blueprint(ubp, url_prefix='/users')

    return app