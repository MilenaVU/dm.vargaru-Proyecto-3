from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, Usuario, Producto, Ingrediente

bp = Blueprint('main', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Usuario.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Login exitoso', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'danger')
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión', 'info')
    return redirect(url_for('main.login'))

@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/productos')
@login_required
def productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@bp.route('/producto/<int:producto_id>')
@login_required
def producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    return render_template('producto.html', producto=producto)

@bp.route('/ingredientes')
@login_required
def ingredientes():
    ingredientes = Ingrediente.query.all()
    return render_template('ingredientes.html', ingredientes=ingredientes)

@bp.route('/ingrediente/<int:ingrediente_id>')
@login_required
def ingrediente(ingrediente_id):
    ingrediente = Ingrediente.query.get_or_404(ingrediente_id)
    return render_template('ingrediente.html', ingrediente=ingrediente)

@bp.route('/sell_producto/<int:producto_id>', methods=['POST'])
@login_required
def sell_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    if producto.cantidad > 0:
        producto.cantidad -= 1
        db.session.commit()
        flash('Producto vendido exitosamente', 'success')
    else:
        flash('Producto fuera de stock', 'danger')
    return redirect(url_for('main.productos'))

@bp.route('/replenish_producto/<int:producto_id>', methods=['POST'])
@login_required
def replenish_producto(producto_id):
    producto = Producto.query.get_or_404(producto_id)
    cantidad = request.form.get('cantidad', type=int)
    producto.cantidad += cantidad
    db.session.commit()
    flash('Producto reabastecido exitosamente', 'success')
    return redirect(url_for('main.productos'))


#Rutas segun nivel usuairo
# Rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = user.username
            session['es_admin'] = user.es_admin
            flash('Inicio de sesión exitoso!')
            return redirect(url_for('venta'))
        else:
            flash('Nombre de usuario o contraseña incorrectos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('es_admin', None)
    flash('Has cerrado sesión.')
    return redirect(url_for('index'))

@app.route('/venta')
@login_required
@admin_required
def venta():
    productos = Producto.query.all()
    return render_template('venta.html', productos=productos)

