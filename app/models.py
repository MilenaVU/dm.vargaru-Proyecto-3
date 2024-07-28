from app import db
from flask_login import UserMixin
#definicion de clases para llamr los datos de la BD

#Clase usuario
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)
    es_empleado = db.Column(db.Boolean, default=False)

    def get_id(self):
        return str(self.id)

#Clase tbl producto
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    calorias = db.Column(db.Integer, nullable=False)
    costo_produccion = db.Column(db.Float, nullable=False)
    rentabilidad = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Producto {self.nombre}>'

#Clase tbl ingrediente
class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)
    saludable = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Ingrediente {self.nombre}>'

# Proteger rutas acceso segun nivel usuarios
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session or not session.get('es_admin'):
            flash('Acceso denegado: Solo administradores pueden realizar ventas.')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
