from flask import Flask, request, send_file

app = Flask(__name__)


@app.route('/')
def index():

    return 'Home page'


@app.route('/greet', methods=['GET','POST'])
def greet():

    name = request.args.get('name', 'Guest')
    msg = f'Hello {name}'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}

@app.route('/get_sid')
def get_image():

    filename = 'sid.jpg'
    return send_file(filename, mimetype='image/jpg')


# curl localhost:5000/greet?name=Peter
# Hello Peter

# curl localhost:5000/greet
# Hello Guest