from flask import Blueprint, render_template, request, jsonify

main_page = Blueprint('page', __name__)
hello_page = Blueprint('hello', __name__)
square_page = Blueprint('square', __name__)
status_page = Blueprint('status', __name__)
math = Blueprint('math', __name__)
calc_page = Blueprint('calc', __name__)

@main_page.route('/')
def hello():
    return 'For super Earth!'


@hello_page.route('/hello/<name>')
def hello_name(name):
    return f"A new warrior({name}) for the Horde!"


@square_page.route('/square/<int:number>')
def square(number):
    return str(number * number)


@status_page.route('/status')
def json_status():
    status = {
    "status": "running",
    "service": "Flask App"
    }
    return jsonify(status)


@math.route('/math')
def calculator():

    operation= request.args.get('operation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    match(operation):
        case "+":
            result = str(num1 + num2)
            return result
        case "-":
            result = str(num1 - num2)
            return result
        case " /":
            result = str(num1 / num2)
            return result
        case "*":
            result = str(num1 * num2)
            return result
    return " "
   

@calc_page.route('/calc')
def render():
    return render_template("calculator_page.html")