from flask import Flask

app = Flask(__name__)


@app.errorhandler(404)
def error_404(e):
    return '<h1>No source like your request.</h1>', 404


@app.route('/')
def index():
    return '<h1>Test app</h1>'


if __name__ == '__main__':
    app.run(debug=True, port=5000)

    # Here you can pass any parameters you want.
    # It will not affect the application work.
