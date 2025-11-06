'''
flask
'''

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''<h1>Welcome to the HTTP Status Codes Info Site</h1>
    <a href="/errors">View HTTP Status Codes</a>
    <br>
    <a href="/about">About</a>
    '''


@app.route('/errors')
def errors():
    return '''
    <h1>HTTP Status Codes</h1>
    <ul>
        <li><a href="/error/400">400 Bad Request</a></li>
        <li><a href="/error/401">401 Unauthorized</a></li>
        <li><a href="/error/403">403 Forbidden</a></li>
        <li><a href="/error/404">404 Not Found</a></li>
    </ul>
    <a href="/about">About</a>
    <br>
    <a href="/">Back</a>
    '''

@app.route('/about')
def about():
    return '''
    <h1>About</h1>
    <p>This site provides information about common HTTP status codes.</p>
    <a href="https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP">Information Source</a>
    <br>
    <a href="/errors">View HTTP Status Codes</a>
    <a href="/">Back</a>
    '''

@app.route('/error/400')
def error_400():
    return '''
    <h1>400 Bad Request</h1>
    <p>The server could not understand the request due to invalid syntax.</p>
    <a href="/errors">Back</a>
    '''

@app.route('/error/401')
def error_401():
    return '''
    <h1>401 Unauthorized</h1>
    <p>The client must authenticate itself to get the requested response.</p>
    <a href="/errors">Back</a>
    '''

@app.route('/error/403')
def error_403():
    return '''
    <h1>403 Forbidden</h1>
    <p>The client does not have access rights to the content.</p>
    
    <a href="/errors">Back</a>
    '''

@app.route('/error/404')
def error_404():
    return '''
    <h1>404 Not Found</h1>
    <p>The server can not find the requested resource.</p>
    <a href="/errors">Back</a>
    '''

if __name__ == '__main__':
    app.run(debug=True) 