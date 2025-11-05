'''
flask
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Error 11093923919"

@app.route('/about')
def about():
    return "My name is Kylych"

@app.route('/help')
def help():
    return "Use /about to learn more about me."

if __name__ == '__main__':
    app.run(debug=True) 