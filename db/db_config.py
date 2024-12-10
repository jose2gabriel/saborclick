import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados SQLAlchemy
DATABASE_URL = "postgresql://postgres:1712@localhost:5432/codethor?schema=public"

# Criando a instância do engine para conexão
engine = create_engine(DATABASE_URL, echo=True)  # echo=True para debug/logging no SQLAlchemy
Base = declarative_base()

# Configuração de sessão com SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Configuração do logger para monitoramento de operações
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def conectar_banco_sqlalchemy():
    """Função para conectar ao banco de dados com SQLAlchemy"""
    try:
        with engine.connect() as connection:
            logger.info("Conexão com o banco de dados estabelecida com sucesso usando SQLAlchemy!")
    except Exception as e:
        logger.error(f"Erro ao conectar ao banco de dados com SQLAlchemy: {e}")


def fechar_conexao_sqlalchemy():
    """Função para fechar a conexão com o banco de dados usando SQLAlchemy"""
    logger.info("Conexão com o banco de dados fechada com sucesso!")


def criar_tabelas_sqlalchemy():
    """Função para criar todas as tabelas no banco com SQLAlchemy"""
    try:
        conectar_banco_sqlalchemy()

        from models.produto import Produto
        from models.categoria import Categoria
        from models.usuario import Usuario

        Base.metadata.create_all(bind=engine)
        logger.info("Tabelas criadas com sucesso usando SQLAlchemy!")

    except Exception as e:
        logger.error(f"Erro ao criar tabelas no banco com SQLAlchemy: {e}")
    finally:
        fechar_conexao_sqlalchemy()


def get_db():
    """
    Função que cria e gerencia a sessão do banco de dados de forma global.
    Garante que todas as operações usem a mesma sessão de maneira segura.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        logger.error(f"Erro ao gerenciar sessão do banco de dados: {e}")
        raise
    finally:
        db.close()
