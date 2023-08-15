from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_answer():
    return '42'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
