from flask import Flask

app = Flask(__name__)

@app.route('/') # route 경로를 적어주는 역할을 한다
def hello():
    return 'hello'

@app.route('/sechan')
def checkseachan():
    sechan = 'seachan'
    return sechan

if __name__ == '__main__':
    app.run()