from os.path import abspath, join, sep
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, Session


db_path = join(abspath(__file__).rsplit(sep, maxsplit=1)[0], "database.db")
engine = create_engine(
    f'sqlite:///{db_path}', echo=True)
_Base = declarative_base()
session = sessionmaker(bind=engine)  # , expire_on_commit=False, autocommit=False)


def create_session() -> Session:
    return session()


class Base(_Base):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
