@app.route('/')
def index():
    return 'For Super Earth!'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route/square/<int:number>