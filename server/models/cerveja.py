from sqlalchemy import Column, Integer, String, Numeric

from server.config.database import Base


class Cerveja(Base):
    __tablename__ = 'tb_cerveja'

    id = Column(Integer, primary_key=True)
    estilo = Column(String)
    nome = Column(String)
    teor_alcoolico = Column(Numeric)



