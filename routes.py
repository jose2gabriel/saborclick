from flask import Blueprint
from controllers.usuario_controller import UsuarioController
from controllers.produto_controller import ProdutoController
from controllers.categoria_controller import CategoriaController
from controllers.cardapio_controller import CardapioController
from auth.token_required import token_required  # Importando o token_required

# Registro das rotas
usuario = Blueprint('usuario', __name__, url_prefix='/usuario')
usuario.route('/cadastrar', methods=['POST'])(UsuarioController.criar_usuario)
usuario.route('/login', methods=['POST'])(UsuarioController.login)

# Registro das rotas
produto = Blueprint('produto', __name__, url_prefix='/produto')
produto.route('/', methods=['GET'])(token_required(ProdutoController.listar_produtos))
produto.route('/novo', methods=['POST'])(token_required(ProdutoController.criar_produto))


# Registro das rotas
categoria = Blueprint('categoria', __name__, url_prefix='/categoria')
categoria.route('/', methods=['GET'])(token_required(CategoriaController.listar_categoria))
categoria.route('/novo', methods=['POST'])(token_required(CategoriaController.criar_catetoria))


# Registro das rotas
cardapio = Blueprint('cardapio', __name__, url_prefix='/cardapio')
cardapio.route('/', methods=['GET'])(token_required(CardapioController.listar_produtos_com_categorias))


# Função para inicializar as rotas
def init_routes(app):
    app.register_blueprint(usuario)
    app.register_blueprint(produto)
    app.register_blueprint(categoria)
    app.register_blueprint(cardapio)
