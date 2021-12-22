from flask import Flask

app = Flask(__name__)


@app.route('/')
def HelloWorld():
    return '<h1>사이트 정상작동 확인!'
