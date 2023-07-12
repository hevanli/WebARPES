from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    Bootstrap(app)

    from app.frontend import frontendbp
    app.register_blueprint(frontendbp)
    return app
