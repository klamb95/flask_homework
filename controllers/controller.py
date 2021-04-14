from flask import render_template
from app import app
from modules.calculator import *

@app.route('/add/<num_1>/<num_2>')
def addition(num_1,num_2):
    answer = add_two_numbers(int(num_1), int(num_2))
    return render_template('addition.html', answer=answer )

@app.route('/minus/<num_1>/<num_2>')
def subtraction(num_1,num_2):
    answer = subtract_two_numbers(int(num_1), int(num_2))
    return render_template('subtraction.html', answer=answer )

@app.route('/times/<num_1>/<num_2>')
def multipy(num_1,num_2):
    answer = multiply_two_numbers(int(num_1), int(num_2))
    return render_template('multiply.html', answer=answer )

@app.route('/divide/<num_1>/<num_2>')
def divide(num_1,num_2):
    answer = divide_two_numbers(int(num_1), int(num_2))
    return render_template('divide.html', answer=answer )

