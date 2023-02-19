from .base_meta import Base
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER


class Hulls(Base):
    __tablename__ = "hulls"

    hull = Column(Text, primary_key=True)
    armor = Column(INTEGER(unsigned=True), nullable=False)
    type = Column(INTEGER(unsigned=True), nullable=False)
    capacity = Column(INTEGER(unsigned=True), nullable=False)

    def __repr__(self) -> str:
        return f"{self.hull}, armor='{self.armor}', type='{self.type}," \
               f" capacity='{self.capacity}'"
