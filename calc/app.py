from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)

math_functions = {
    'add' : add,
    'sub' : sub,
    'div' : div,
    'mult': mult
}

@app.route('/add')
def call_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)
    
@app.route('/sub')
def call_sub():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route('/div')
def call_div():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)

@app.route('/mult')
def call_mult():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route('/math/<operation>')
def call_operation(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = math_functions[operation](a,b)
    return str(result)


  