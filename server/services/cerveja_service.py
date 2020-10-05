from server.models import cerveja
from server.repositories.cerveja_repository import CervejaRepository
from server.schemas import cerveja_schema


class CervejaService:

    def __init__(self):
        self.cerveja_repository = CervejaRepository()

    def get_cervejas(self):
        return self.cerveja_repository.get_cervejas()

    def create_cerveja(self, cerveja_dto: cerveja_schema.CervejaCreate):
        db_cerveja = cerveja.Cerveja(
            estilo=cerveja_dto.estilo,
            nome=cerveja_dto.nome,
            teor_alcoolico=cerveja_dto.teor_alcoolico
        )

        return self.cerveja_repository.save_obj(db_cerveja)
