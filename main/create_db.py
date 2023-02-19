from os.path import exists
from database import db_path, Base, engine
from fill_db import FillDb


class CreationDb:
    @staticmethod
    def create_db() -> None:
        filler = FillDb()
        if not exists(db_path):
            Base.metadata.create_all(bind=engine)
            filler.fill_db()
