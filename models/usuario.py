from sqlalchemy import Column, Integer, String
from db.db_config import Base
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(Base):
    __tablename__ = "usuario"
    
    _id = Column(Integer, name='id', primary_key=True)
    _nome = Column(String, name='nome', nullable=False)
    _senha = Column(String, name='senha', nullable=False)
    _email = Column(String, name='email', nullable=False, unique=True)

    def set_senha_segura(self, senha):
        self._senha = generate_password_hash(senha)

    def validar_senha(self, senha):
        return check_password_hash(self._senha, senha)

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_nome(self):
        return self._nome

    def set_nome(self, value):
        self._nome = value

    def get_senha(self):
        return self._senha

    def set_senha(self, value):
        self.set_senha_segura(value)

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def usuario(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email()
        }
