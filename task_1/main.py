from flask import Flask, render_template
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

@app.route('/calc')
def calculator():
    return render_template("html.html")
    
if __name__ == '__main__':
    app.run(debug=True)