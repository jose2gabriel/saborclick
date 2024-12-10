from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.db_config import Base

class Categoria(Base):
    __tablename__ = 'categoria'

    _id = Column(Integer, name='id', primary_key=True)
    _codigo = Column(String, name='codigo', nullable=False)
    _descricao = Column(String, name='descricao', nullable=False)

    # Relacionamento com Produto
    produtos = relationship("Produto", back_populates="categoria")

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
        
    def categoria(self):
        return {
            "id": self.get_id(),
            "codigo": self.get_codigo(),
            "descricao": self.get_descricao(),
        }