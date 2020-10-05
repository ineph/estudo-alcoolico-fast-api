from pydantic.main import BaseModel


class CervejaBase(BaseModel):
    estilo: str
    nome: str
    teor_alcoolico: float


class CervejaCreate(CervejaBase):
    pass


class Cerveja(BaseModel):
    id: int
