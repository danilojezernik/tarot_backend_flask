from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_index():
    return 'Hello World! Haha'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004, debug=True)
