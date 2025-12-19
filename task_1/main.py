from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'For super Earth!'

@app.route('/hello/<name>')
def hello_name(name):
    return f"A new warrior({name}) for the Horde!"

@app.route('/square/<int:number>')
def square(number):
    return str(number * number)

@app.route('/status')
def json_status():
    status = {
    "status": "running",
    "service": "Flask App"
    }
    return jsonify(status)

@app.route('/math')
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
   

@app.route('/calc')
def render():
    return render_template("html.html")

if __name__ == '__main__':
    app.run(debug=True)