from server import db_session


class BaseRepository:
    def __init__(self):
        self.db = db_session

    def save_obj(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
