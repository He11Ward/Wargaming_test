from os.path import exists, abspath, sep, join
from random import choice, randint
from pytest import fixture, mark
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session
from database import Base, Ships, Hulls, Weapons, Engines, create_session as sessionmaker_src


@fixture(scope='session')
def temp_db():
    db_path = join(abspath(__file__).rsplit(sep, maxsplit=1)[0], "../main/database_temp.db")
    new_engine = create_engine(
        f'sqlite:///{db_path}', echo=True)

    sessionmaker_dst = sessionmaker(bind=new_engine)

    if not exists(db_path):
        Base.metadata.create_all(bind=new_engine)

        session_src: Session = sessionmaker_src()
        session_dst = sessionmaker_dst()

        for entity in [Hulls, Weapons, Engines]:
            rows = session_src.query(entity).all()
            for row in rows:
                dict_obj = row.to_dict()
                editable_keys = list(dict_obj.keys())
                editable_keys.remove(entity.__name__.lower()[:-1])
                dict_obj[choice(editable_keys)] = randint(1, 20)
                new_obj = entity(**dict_obj)
                session_dst.add(new_obj)
        session_dst.commit()

        ships_src = session_src.query(Ships).all()
        for ship in ships_src:
            dict_obj = ship.to_dict()
            new_obj = Ships(**dict_obj)
            session_dst.add(new_obj)
        session_dst.commit()

        ships_dst = session_dst.query(Ships).all()
        for ship in ships_dst:
            ship: Ships
            cls, cls_name = choice([(Hulls, "hull"), (Weapons, "weapon"), (Engines, "engine")])
            random_entity = session_dst.query(cls).order_by(func.random()).first()
            print(ship.ship, ship.__getattribute__(cls_name), cls_name, random_entity.__getattribute__(cls_name))
            ship.__setattr__(cls_name, random_entity.__getattribute__(cls_name))
            session_dst.commit()
    else:
        session_src: Session = sessionmaker_src()
        session_dst = sessionmaker_dst()
    yield session_src, session_dst
    session_src.close()
    session_dst.close()


"""@mark.xfail"""


@mark.parametrize("row_name, column, column_model, column_name",
                  [("Ship-{}".format(i), "weapon", Weapons, Weapons.weapon) for i in range(1, 201)] +
                  [("Ship-{}".format(i), "hull", Hulls, Hulls.hull) for i in range(1, 201)] +
                  [("Ship-{}".format(i), "engine", Engines, Engines.engine) for i in range(1, 201)])
def test_ships_table(temp_db, row_name, column, column_model, column_name):
    session_src, session_dst = temp_db
    ship_data_src = session_src.query(Ships).where(Ships.ship == row_name).first()
    ship_data_dst = session_dst.query(Ships).where(Ships.ship == row_name).first()
    column_data_src = session_src.query(column_model).where(column_name == ship_data_src.to_dict()[column]).first()
    column_data_dst = session_dst.query(column_model).where(column_name == ship_data_src.to_dict()[column]).first()
    assert (ship_data_src == ship_data_dst), f"{ship_data_src} expected, \n {ship_data_dst} found"
    assert (column_data_src == column_data_dst), f"{column_data_src} expected, \n {column_data_dst} found"
