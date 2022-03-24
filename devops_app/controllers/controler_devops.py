from flask import Flask, make_response, request,jsonify
from authlib.jose import jwt
from __init__ import app 
from functools import wraps
from datetime import datetime

def generate_token():
    return jwt.encode(
        {'alg': 'RS256'},
        {'iat': datetime.utcnow(), 'API_KEY': app.config['API_KEY']},
        app.config.get('PRIVATE_KEY')
    ).decode()

def decode_token(token):
    try:
        return jwt.decode(token, app.config.get('PUBLIC_KEY'))
    except:
        return None


def require_tokenJWT(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        token = decode_token(request.headers.get("X-JWT-KWY"))
        if token:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify({'error': 'Missing token'}), 401)
    
    return decorated_function


def require_APIkey(view_function):
    def decorated_function(*args, **kwargs):
        if (request.headers.get("X-Parse-REST-API-Key") == app.config['API_KEY']):
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify({'error': 'Missing API key'}), 401)
    return decorated_function


@app.route('/get_token', methods=['GET'])
def get_token():
    token = generate_token()
    return jsonify({'token': token})


@app.route('/DevOps', methods=['POST'])
@require_tokenJWT
@require_APIkey
def message_devops():
    if request.is_json:
        req =  request.get_json()
        response_body = {
            "message": "Hello " + req.get("to") + " your message will be send to DevOps team",

        }
        res = make_response(jsonify(response_body), 200)
        return res
    else:
        return make_response(jsonify({"message": "Request body must be JSON"}), 400)

@app.errorhandler(404)
def not_found(error):
    return 'ERROR'




    


    


