from server.models import cerveja


class CervejaRepository:

    def get_cervejas(self):
        return self.db.query(cerveja.Cerveja).all()
