from flask import Flask, jsonify
from flask import make_response, abort, request
from flask_httpauth import HTTPBasicAuth
from flask_cors import *
from Utils.db import Database
from Utils.InterfaceTest import InterfaceTest

app = Flask(__name__)
CORS(app, supports_credentials = True)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    if username == 'mar':
        return 'python'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/tasks', methods = ['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/interface/add', methods = ['POST'])
def add_interface():
    if not request.json:
        abort(404)
    ServiceUrl = request.json['url']
    Environment = request.json['env']
    Method = request.json['method']
    Parameters = request.json['param']
    Comment = request.json['comment']

    sql = "INSERT INTO `sis_interface` (ServiceUrl, Environment, Method, Parameters, Comment) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}');".format(
        ServiceUrl, Environment, Method, Parameters, Comment)

    db = Database()

    db.insert(sql)

    return jsonify({'state': 'Success.'})


@app.route('/api/result', methods = ['GET'])
def get_interface_info():
    sql = "SELECT ServiceUrl AS reqUrl,Environment AS env,Method AS method,Parameters AS reqParam,Comment AS comment FROM sis_interface;"
    db = Database()
    info = db.query(sql)
    interfaceTest = InterfaceTest()
    result = []
    respResult = None
    for i in info:
        reqUrl = i['reqUrl']
        method = i['method']
        reqParam = i['reqParam']
        expectInfo = 0
        respResult = interfaceTest.test_interface(method, reqUrl, reqParam, expectInfo)
        result.append(respResult)

    return jsonify({'finalResult': respResult, 'detailResult': result})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found.'}), 404)


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
