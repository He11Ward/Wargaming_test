from database.ships import Ships
from database.weapons import Weapons
from database.hulls import Hulls
from database.engines import Engines
from database.base_meta import create_session
from random import randint


class FillDb:
    def __init__(self):
        self.ships_amount = 200
        self.weapons_amount = 20
        self.hulls_amount = 5
        self.engines_amount = 6
        self.rand_start = 1
        self.rand_end = 20

    def fill_db(self):
        session = create_session()
        self.fill_weapons(session)
        self.fill_hulls(session)
        self.fill_engines(session)
        self.fill_ships(session)
        session.close()

    def fill_weapons(self, session):
        for i in range(self.weapons_amount):
            row_to_add = Weapons(weapon=f"Weapon-{i+1}", reload_speed=randint(self.rand_start, self.rand_end),
                                 rotational_speed=randint(self.rand_start, self.rand_end),
                                 diameter=randint(self.rand_start, self.rand_end),
                                 power_volley=randint(self.rand_start, self.rand_end),
                                 count=randint(self.rand_start, self.rand_end))
            session.add(row_to_add)
        session.commit()

    def fill_hulls(self, session):
        for i in range(self.hulls_amount):
            row_to_add = Hulls(hull=f"Hull-{i+1}", armor=randint(self.rand_start, self.rand_end),
                               type=randint(self.rand_start, self.rand_end),
                               capacity=randint(self.rand_start, self.rand_end))
            session.add(row_to_add)
        session.commit()

    def fill_engines(self, session):
        for i in range(self.engines_amount):
            row_to_add = Engines(engine=f"Engine-{i+1}", power=randint(self.rand_start, self.rand_end),
                                 type=randint(self.rand_start, self.rand_end))
            session.add(row_to_add)
        session.commit()

    def fill_ships(self, session):
        for i in range(self.ships_amount):
            row_to_add = Ships(ship=f"Ship-{i + 1}", weapon=f"Weapon-{randint(1, self.weapons_amount)}",
                               hull=f"Hull-{randint(1, self.hulls_amount)}",
                               engine=f"Engine-{randint(1, self.engines_amount)}")
            session.add(row_to_add)
        session.commit()
