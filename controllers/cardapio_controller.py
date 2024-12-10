from flask import jsonify
from db.db_config import get_db
from models.produto import Produto
from models.categoria import Categoria

class CardapioController:
    @staticmethod
    def listar_produtos_com_categorias():
        with next(get_db()) as db:
            try:
                categorias = db.query(Categoria).all()
                
                resultado = []
                for categoria in categorias:
                    produtos = db.query(Produto).filter(Produto._categoria == categoria.get_id()).all()
                    resultado.append({
                        "categoria": {
                            "id": categoria.get_id(),
                            "codigo": categoria.get_codigo(),
                            "descricao": categoria.get_descricao(),
                        },
                        "produtos": [
                            {
                                "id": produto.get_id(),
                                "codigo": produto.get_codigo(),
                                "descricao": produto.get_descricao(),
                            }
                            for produto in produtos
                        ]
                    })

                return jsonify(resultado)
            except Exception as e:
                return jsonify({"message": f"Erro ao buscar produtos e categorias: {str(e)}"}), 500