from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .views import users_blueprint
    app.register_blueprint(users_blueprint)
    
    return app