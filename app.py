from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return "Hello World"


@app.route('/about')
def about():
    return "About company"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User name: " + name + " - id: " + str(id)


if __name__ == "__main__":
    app.run()
