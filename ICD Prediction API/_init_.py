from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import users, errors, tokens

def create_app(config_class=Config):
    app = Flask(__name__)
    
    from app.api import bp as api_bp
    app.register_blueprint(bp)

    return app