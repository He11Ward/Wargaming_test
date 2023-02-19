from .base_meta import Base
from sqlalchemy import Column, Text
from sqlalchemy.dialects.mysql import INTEGER


class Engines(Base):
    __tablename__ = "engines"

    engine = Column(Text, primary_key=True)
    power = Column(INTEGER(unsigned=True), nullable=False)
    type = Column(INTEGER(unsigned=True), nullable=False)

    def __repr__(self):
        return f"{self.engine}, power='{self.power}', type='{self.type}'"
