from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)

    Bootstrap(app)

    from app.frontend import frontendbp
    app.register_blueprint(frontendbp)
    return app
