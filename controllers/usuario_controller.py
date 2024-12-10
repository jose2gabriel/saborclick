from flask import jsonify, request
from db.db_config import get_db
from dto.usuario_dto import UsuarioDto
from models.usuario import Usuario
from auth.token_required import gerar_token

db = next(get_db())

class UsuarioController:

    @staticmethod
    def criar_usuario():
        try:
            dados_request = request.get_json()
            usuario_dto = UsuarioDto.from_request(dados_request)

            usuario = Usuario()
            usuario.set_nome(usuario_dto.get_nome())
            usuario.set_email(usuario_dto.get_email())
            usuario.set_senha(usuario_dto.get_senha().strip())

            db.add(usuario)
            db.commit()
            db.refresh(usuario)

            return jsonify(usuario.usuario())
        
        except Exception as e:
            return jsonify({'message': f'Erro ao criar usuário: {str(e)}'}), 500

    @staticmethod
    def login():
        try:
            dados_request = request.get_json()
            usuario_dto = UsuarioDto.from_request(dados_request)

            if not usuario_dto.get_email() or not usuario_dto.get_senha():
                return jsonify({"message": "Email ou senha não fornecidos"}), 400

            usuario = db.query(Usuario).filter(Usuario._email == usuario_dto.get_email()).first()

            if not usuario:
                return jsonify({"message": "Usuário não encontrado"}), 401

            senha_informada = usuario_dto.get_senha().strip()
            if usuario.validar_senha(senha_informada):
                token = gerar_token(usuario.get_id())
                return jsonify({
                    "message": "Login bem-sucedido",
                    "token": token,
                    "usuario": usuario.usuario()
                }), 200
            else:
                return jsonify({"message": "Senha inválida"}), 401

        except Exception as e:
            return jsonify({"message": f"Erro ao processar login: {str(e)}"}), 500
