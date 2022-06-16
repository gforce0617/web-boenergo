import math
import random
from app import app
from flask import render_template
from app.forms import EquationForm, ColorForm


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def solve():
    form = EquationForm()
    if form.validate_on_submit():
        a = form.a.data
        b = form.b.data
        c = form.c.data
        if b*b - 4*a*c < 0:
            solution = "Нет решений"
        elif b*b - 4*a*c == 0:
            solution = "x= " + str(-b/(2*a))
        else:
            x1 = (-b + math.sqrt(b*b - 4*a*c))/(2*a)
            x2 = (-b - math.sqrt(b*b - 4*a*c))/(2*a)
            solution = "x1= " + str(x1) + " " + "x2= " + str(x2)
        return render_template('index.html', title="Home", form=form, solution=solution)
    solution = ""
    return render_template('index.html', title="Home", form=form, solution=solution)


@app.route('/2', methods=['GET', 'POST'])
def define():
    form = ColorForm()
    if form.validate_on_submit():
        n = form.n.data
        rand = random.random()
        if rand <=0.6:
            solution = "Синий"
        elif 0.6 < rand <= 0.82:
            solution = "Зеленый"
        else:
            solution = "Красный"
        return render_template('2.html', title="Home", form=form, solution=solution)
    solution = ""
    return render_template('2.html', title="Home", form=form, solution=solution)