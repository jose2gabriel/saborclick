from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.db_config import Base

from .categoria import Categoria

class Produto(Base):
    __tablename__ = 'produto'

    _id = Column(Integer, name='id', primary_key=True)
    _codigo = Column(String, name='codigo', nullable=False)
    _descricao = Column(String, name='descricao', nullable=False)
    _categoria = Column(Integer, ForeignKey('categoria.id'), name='id_categoria', nullable=False)
    _valor = Column(Numeric(10, 2), name='valor', nullable=False)

    # Relacionamento com Categoria
    categoria = relationship("Categoria", back_populates="produtos")

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_codigo(self):
        return self._codigo

    def set_codigo(self, value):
        self._codigo = value

    def get_descricao(self):
        return self._descricao

    def set_descricao(self, value):
        self._descricao = value
        
    def get_categoria(self):
        return self.categoria

    def set_categoria(self, value):
        self.categoria = value

    def get_valor(self):
        return self._valor

    def set_valor(self, value):
        self._valor = value

    def produto(self):
        return {
            "id": self.get_id(),
            "codigo": self.get_codigo(),
            "descricao": self.get_descricao(),
            "valor": self.get_valor(),
            "categoria": {
                "id": self.categoria.get_id(),
                "codigo": self.categoria.get_codigo(),
                "descricao": self.categoria.get_descricao()
            } if self.categoria else None
        }