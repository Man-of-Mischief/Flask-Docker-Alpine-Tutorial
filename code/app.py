from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1><center>This is Flask Application - Version 1</center></h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
