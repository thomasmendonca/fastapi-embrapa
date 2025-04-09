import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carrega variáveis do .env
load_dotenv()

# URL de conexão com o banco MySQL (formato: mysql+pymysql://usuário:senha@host:porta/banco)
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria a engine de conexão com o banco de dados, engine é o ponto central de conexão com o banco
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
# Todas as classes de modelo herdarão desta classe
Base = declarative_base()

# Função geradora que fornece sessões de banco de dados
def get_db():
    # Cria uma nova sessão
    db = SessionLocal()
    try:
        # Entrega a sessão para uso
        yield db
    finally:
        # Garante que a sessão será fechada após o uso
        # Mesmo se ocorrer um erro durante a operação
        db.close()