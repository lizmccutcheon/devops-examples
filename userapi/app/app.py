from flask import Flask, render_template, request, Response
from flask_swagger_ui import get_swaggerui_blueprint
import sqlite3
import json
import services.api_services
from model.api_models import *
from services.api_services import *

### initialize sqlite db
init_db()

### create Flask app
app = Flask(__name__)

### configure Swagger
swagger_url = '/swagger'
api_url = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    swagger_url,
    api_url,
    config={
        'app_name': "My Stupid Flask API",
        'validatorUrl': 'none'
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=swagger_url)

### define API routes
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/hello', methods=['GET'])
def hello_world():
    response = Response(json.dumps({"Hello":"world"}),200, mimetype='application/json')
    return response


@app.route('/health', methods=['GET'])
def ping():
    check = healthcheck()
    if check != None:
        response = Response("OK", 200, mimetype='text/plain')
        return response
    else:
        return Response("Something has gone wrong", 500, mimetype='text/plain')


@app.route('/users', methods=['GET'])
def get_all_users():
    response = Response(get_users(),200, mimetype='application/json')
    return response


@app.route('/users', methods=['POST'])
def create_new_user():
    try:
        request_data = request.get_json()
        username = request_data["username"]
        firstname = request_data["firstname"]
        lastname = request_data["lastname"]
    except:
        response = Response("Bad request", 400, mimetype='text/plain')
    else:
        if (len(username) == 0 or len(firstname) == 0 or len(lastname) == 0):
            response = Response("Bad request", 400, mimetype='text/plain')
        elif get_user(request_data["username"]):
            response = Response("User already exists", 409, mimetype='text/plain')
        else:
            add_user(username,firstname,lastname)
            response = Response("User added", 201, mimetype='text/plain')
    return response


@app.route('/users/<username>', methods=['GET'])
def get_one_user(username):
    if get_user(username):
        response = Response(get_user(username),200, mimetype='application/json')
    else:
        response = Response("User does not exist",404,mimetype='text/plain')
    return response


@app.route('/users/<username>', methods=['DELETE'])
def delete_one_user(username):
    if (len(username) > 0):
        if (get_user(username)):
            delete_user(username)
            response = Response("User deleted", 200, mimetype='text/plain')
        else:
            response = Response("User does not exist", 404, mimetype='text/plain')
    else:
        response = Response("Bad request", 400, mimetype='text/plain')
    return response


@app.route('/users/<username>', methods=['POST'])
def edit_user(username):
    try:
        request_data = request.get_json()
        p_username = request_data["username"]
        p_firstname = request_data["firstname"]
        p_lastname = request_data["lastname"]
    except:
        response = Response("Bad request", 400, mimetype='text/plain')
    else:
        if p_username != username: # username in url doesn't match posted data
            response = Response("Bad request", 400, mimetype='text/plain')
        elif (len(p_username) == 0 or len(p_firstname) == 0 or len(p_lastname) == 0):
            response = Response("Bad request", 400, mimetype='text/plain')
        elif get_user(p_username): # user exists - update them
            update_user(p_username,p_firstname,p_lastname)
            response = Response("User updated", 201, mimetype='text/plain')
        else:
            response = Response("User does not exist", 404, mimetype='text/plain')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
