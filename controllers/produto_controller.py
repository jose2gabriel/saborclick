from flask import jsonify, request
from dto.produto_dto import ProdutoDto

from models.produto import Produto
from models.categoria import Categoria
from db.db_config import get_db

db = next(get_db())

class ProdutoController:
    
    @staticmethod
    def criar_produto():
        dados_request = request.get_json()        
        produto_dto = ProdutoDto.from_request(dados_request)
        
        try:
            categoria = db.query(Categoria).filter(Categoria._id == produto_dto.get_categoria().get_id()).one_or_none()
            
            print(categoria.get_descricao())

            if not categoria:
                return jsonify({'message': 'Categoria não encontrada'}), 404
            
            
            print(categoria.get_descricao())
            
            produto = Produto()
            produto.set_codigo(produto_dto.get_codigo())
            produto.set_descricao(produto_dto.get_descricao())
            produto.set_categoria(categoria)
            produto.set_valor(produto_dto.get_valor())

            db.add(produto)
            db.commit()
            db.refresh(produto)
            return jsonify(produto.produto())
        except Exception as e:
            return jsonify({'message': f'Erro ao criar produto: {str(e)}'}), 500

    
    @staticmethod 
    def listar_produtos():
        try:
            db = next(get_db())
                        
            produtos = db.query(Produto).all()
            
            produtos_list = []
            for produto in produtos:
                produtos_list.append({
                    "id": produto.get_id(),
                    "nome": produto.get_descricao(),
                    "preco": produto.get_valor(),
                })
            
            return jsonify(produtos_list)        
        except Exception as e:
            return jsonify({'message': f'Erro ao listar produtos: {str(e)}'}), 500