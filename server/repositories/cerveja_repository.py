from server.models import cerveja
from server.repositories.base_repository import BaseRepository


class CervejaRepository(BaseRepository):

    def get_cervejas(self):
        return self.db.query(cerveja.Cerveja).all()

    def delete_cerveja(self, cerveja_id):
        self.db.query(cerveja.Cerveja).filter(cerveja.Cerveja.id == cerveja_id).delete()
        self.db.commit()


