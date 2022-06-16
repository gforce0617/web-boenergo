from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class EquationForm(FlaskForm):
    a = IntegerField('A', validators=[DataRequired()])
    b = IntegerField('B', validators=[DataRequired()])
    c = IntegerField('C', validators=[DataRequired()])
    solve = SubmitField('Решить')


class ColorForm(FlaskForm):
    n = IntegerField('Введите число', validators=[DataRequired()])
    define = SubmitField('Определить')
