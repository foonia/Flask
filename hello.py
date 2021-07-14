from flask import Flask
from globalpackage import config
from Business import dataflow

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False #json 한국어 가능

@app.route('/') # route 경로를 적어주는 역할을 한다
def hello():
    return 'hello'

@app.route('/sechan')
def checkseachan():
    sechan = 'seachan'
    return sechan

@app.route('/data')
def data():
    print(config.configjson)
    return config.configjson

@app.route('/updatetest')
def update():
    test = dataflow.updateData()
    test.runupdate()
    return "TEST OK"

if __name__ == '__main__':
    app.run()