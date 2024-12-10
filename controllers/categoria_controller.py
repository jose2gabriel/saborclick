from flask import jsonify, request
from dto.categoria_dto import CategoriaDto
from models.categoria import Categoria
from db.db_config import get_db
from sqlalchemy.sql import text

class CategoriaController:
    @staticmethod
    def criar_catetoria():
        dados_request = request.get_json()        
        categoria_dto = CategoriaDto.from_request(dados_request)
        
        categoria = Categoria()
        categoria.set_codigo(categoria_dto.get_codigo())
        categoria.set_descricao(categoria_dto.get_descricao())

        try:
            db = next(get_db())
            db.add(categoria)
            db.commit()
            db.refresh(categoria)
            return jsonify(categoria.categoria())
        except Exception as e:
            return jsonify({'message': f'Erro ao criar produto: {str(e)}'}), 500
    @staticmethod
    def listar_categoria():
        try:
            db = next(get_db())
            query = text("""select id, descricao""")
            query = text(str(query) + """ from categoria""")
            query = text(str(query) + """ where 1 = 1""")
            
            result = db.execute(query)
            categorias = []
            for row in result:
                categorias.append({
                    "id": row.id,
                    "nome": row.descricao
                })
            
            return jsonify(categorias)
        except Exception as e:
            return jsonify({'message': f'Erro ao listar categorias: {str(e)}'}), 500
