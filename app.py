from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Mortgage Project"

@app.route('/calc')
def calc():
    return "This is the mortgage calculator page"

if __name__ == '__main__':
    app.run(debug=True)