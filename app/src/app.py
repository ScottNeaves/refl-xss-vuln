from flask import Flask
from flask import request
import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    if request.args.get('greeting'):
        greeting = base64.b64decode(request.args.get('greeting')).decode('utf-8')
        poorly_sanitized_greeting = greeting.replace("<script>", '').replace("</script>",'')
        return "<html>Hello, and %s</html>!" % poorly_sanitized_greeting
    else:
        return "Hello! You can cause me to echo your favorite greeting by supplying a 'greeting' query param. Get creative with it!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
