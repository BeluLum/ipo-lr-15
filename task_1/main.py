from flask import Flask
from app.routes import main_page, hello_page, square_page, status_page, math, calc_page

app = Flask(__name__)

app.register_blueprint(main_page)
app.register_blueprint(hello_page)
app.register_blueprint(square_page)
app.register_blueprint(status_page)
app.register_blueprint(math)
app.register_blueprint(calc_page)

if __name__ == '__main__':
    app.run(debug=True)