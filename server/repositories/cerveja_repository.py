from server.models import cerveja
from server.repositories.base_repository import BaseRepository


class CervejaRepository(BaseRepository):

    def get_cervejas(self):
        return self.db.query(cerveja.Cerveja).all()
