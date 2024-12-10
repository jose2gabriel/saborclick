import jwt  # Importando a biblioteca PyJWT completa
import datetime
from flask import request, jsonify

SECRET_KEY = 'b65f5da6bc5f2bde389e30db00e484c2'


def gerar_token(usuario_id):
    payload = {
        "user_id": usuario_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token


def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({"message": "Token não fornecido"}), 401

        try:
            if token.startswith("Bearer "):
                token = token[7:]

            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded_token
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper