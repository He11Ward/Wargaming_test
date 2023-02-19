from database.base_meta import Base
from sqlalchemy import Column, ForeignKey, Text
from sqlalchemy.orm import relationship


class Ships(Base):
    __tablename__ = "Ships"

    ship = Column(Text, primary_key=True)
    weapon = Column(Text, ForeignKey('weapons.weapon'), nullable=False)
    hull = Column(Text, ForeignKey('hulls.hull'), nullable=False)
    engine = Column(Text, ForeignKey('engines.engine'), nullable=False)
    weapons = relationship("Weapons", backref="Ships")
    hulls = relationship("Hulls", backref="Ships")
    engines = relationship("Engines", backref="Ships")

    def __repr__(self) -> str:
        return f"{self.ship}, weapon='{self.weapon}', hull='{self.hull}'," \
               f" engine='{self.engine}'"
