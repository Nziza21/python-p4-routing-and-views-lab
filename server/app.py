#!/usr/bin/env python3

# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    return '<br>'.join(str(i) for i in range(parameter))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_operation(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'

    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)