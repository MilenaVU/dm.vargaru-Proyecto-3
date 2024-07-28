from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ch*col4t3.@localhost/heladeria_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Importar modelos y rutas
from .models import Usuario
from .routes import bp as routes_bp

app.register_blueprint(routes_bp)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))
