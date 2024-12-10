from .categoria_dto import CategoriaDto  # Importando corretamente a classe CategoriaDto

class ProdutoDto:
    def __init__(self, codigo, descricao, valor, categoria=None):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        # Aqui você deve armazenar uma instância da CategoriaDto
        self.categoria = CategoriaDto(**categoria) if categoria else None

    @classmethod
    def from_request(cls, request_data):
        """
        Converte os dados da requisição diretamente para um DTO.
        """
        # Transforma os dados da categoria em uma instância de CategoriaDto, caso existam
        categoria_data = request_data.get('categoria')
        return cls(
            codigo=request_data['codigo'],
            descricao=request_data['descricao'],
            valor=request_data['valor'],
            categoria=categoria_data
        )

    @classmethod
    def from_model(cls, produto):
        """
        Converte o modelo Produto para um DTO.
        """
        # Cria uma instância de CategoriaDto a partir do modelo da categoria, caso exista
        return cls(
            codigo=produto.get_codigo(),
            descricao=produto.get_descricao(),
            valor=produto.get_valor(),
            categoria={
                "id": produto.get_categoria().get_id(),
                "codigo": produto.get_categoria().get_codigo(),
                "descricao": produto.get_categoria().get_descricao()
            } if produto.get_categoria() else None
        )

    def to_model(self):
        """
        Converte o DTO de volta para o modelo Produto.
        """
        produto = Produto(
            codigo=self.codigo,
            descricao=self.descricao,
            valor=self.valor
        )
        # Caso a categoria seja definida no DTO, associar ao modelo
        if self.categoria:
            categoria_model = Categoria(
                _id=self.categoria.id,
                _codigo=self.categoria.codigo,
                _descricao=self.categoria.descricao
            )
            produto.set_categoria(categoria_model)
        return produto

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, value):
        self.codigo = value

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, value):
        self.descricao = value

    def get_valor(self):
        return self.valor

    def set_valor(self, value):
        self.valor = value

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, value):
        self.categoria = CategoriaDto(**value) if value else None
