from flask import Flask
app = Flask(__name__)


@app.route('/Hello')
def show_user_profile(username):
    print ("ляляля")
    return 'User %s' % username

@app.route('/')
def greetings():
    return 'For Super Earth!'

if __name__ == '__main__':
    app.run()