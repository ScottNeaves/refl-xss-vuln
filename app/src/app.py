from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    greeting = request.args.get('greeting')
    if greeting:
        return "Hello, and %s!" % greeting
    else:
        return "Hello! You can cause me to echo your favorite greeting by supplying a 'greeting' query param." 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
