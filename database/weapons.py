from .base_meta import Base
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER


class Weapons(Base):
    __tablename__ = "weapons"

    weapon = Column(Text, primary_key=True)
    reload_speed = Column(INTEGER(unsigned=True), nullable=False)
    rotational_speed = Column(INTEGER(unsigned=True), nullable=False)
    diameter = Column(INTEGER(unsigned=True), nullable=False)
    power_volley = Column(INTEGER(unsigned=True), nullable=False)
    count = Column(INTEGER(unsigned=True), nullable=False)

    def __repr__(self):
        return f"{self.weapon}, reload_speed='{self.reload_speed}', rotational_speed='{self.rotational_speed}," \
               f" diameter='{self.diameter}', power_volley='{self.power_volley}', count='{self.count}'"
