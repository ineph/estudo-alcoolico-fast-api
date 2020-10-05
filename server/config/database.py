from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco para o SQLAlchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/postgres"

# cria o engine do SQLAlchemy
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# estancia a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
