
class CategoriaDto:
    def __init__(self, id=None, codigo=None, descricao=None):
        self.id = id
        self.codigo = codigo
        self.descricao = descricao

    @classmethod
    def from_request(cls, request_data):
        """
        Converte os dados da requisição diretamente para um DTO.
        """
        return cls(
            id=request_data.get('id'),  # Usando .get para evitar KeyError
            codigo=request_data.get('codigo'),
            descricao=request_data.get('descricao'),
        )

    @classmethod
    def from_model(cls, produto):
        """
        Converte o modelo Categoria para um DTO.
        """
        return cls(
            id=produto.id,
            codigo=produto.codigo,
            descricao=produto.descricao,
        )

    def to_model(self):
        """
        Converte o DTO de volta para o modelo Categoria.
        """
        return Categoria(
            id=self.id,
            codigo=self.codigo,
            descricao=self.descricao,
        )

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, value):
        self.codigo = value

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, value):
        self.descricao = value
