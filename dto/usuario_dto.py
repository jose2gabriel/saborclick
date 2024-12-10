
class UsuarioDto:
    def __init__(self, id=None, nome=None, email=None, senha=None):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    @classmethod
    def from_request(cls, request_data):
        """
        Converte os dados da requisição diretamente para um DTO.
        Evita KeyError utilizando .get nos campos.
        """
        return cls(
            id=request_data.get('id'),
            nome=request_data.get('nome'),
            email=request_data.get('email'),
            senha=request_data.get('senha')
        )

    @classmethod
    def from_model(cls, usuario):
        """
        Converte o modelo Usuario para um DTO.
        """
        return cls(
            id=usuario.get_id(),
            nome=usuario.get_nome(),
            email=usuario.get_email(),
            senha=usuario.get_senha()
        )

    def to_model(self):
        """
        Converte o DTO de volta para o modelo Usuario.
        """
        return Usuario(
            id=self.id,
            nome=self.nome,
            email=self.email,
            senha=self.senha
        )

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.id = value

    def get_nome(self):
        return self.nome

    def set_nome(self, value):
        self.nome = value

    def get_email(self):
        return self.email

    def set_email(self, value):
        self.email = value

    def get_senha(self):
        return self.senha

    def set_senha(self, value):
        self.senha = value
