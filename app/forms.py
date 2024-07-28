from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')

class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio_publico = FloatField('Precio Público', validators=[DataRequired()])

class IngredienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    calorias = FloatField('Calorias', validators=[DataRequired()])
    inventario = IntegerField('Inventario', validators=[DataRequired()])
    es_vegetariano = BooleanField('Es Vegetariano')
    tipo = SelectField('Tipo', choices=[('base', 'Base'), ('complemento', 'Complemento')], validators=[DataRequired()])
    sabor = StringField('Sabor')  # Only required for Base
