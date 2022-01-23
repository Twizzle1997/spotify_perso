from bottle import route, run
import os

@route('/')
def popularity():
    return 'hello world'


if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)