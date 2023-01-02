from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from db import Base


class TrainingData(Base):
    """Database model for training data"""

    __tablename__ = 'training_data'
    id = Column(Integer(), primary_key=True)
    x = Column(Float(), nullable=False)
    y1 = Column(Float(), nullable=False)
    y2 = Column(Float(), nullable=False)
    y3 = Column(Float(), nullable=False)
    y4 = Column(Float(), nullable=False)

    def __repr__(self) -> str:
        return f"<Data {self.x}>"


class IdeaFunction(Base):
    """ Database model for ideal functions """
    __tablename__ = 'ideal_functions'
    id = Column(Integer(), primary_key=True)
    x = Column(Float(), nullable=False)
    y1 = Column(Float(), nullable=False)
    y2 = Column(Float(), nullable=False)
    y3 = Column(Float(), nullable=False)
    y4 = Column(Float(), nullable=False)
    y5 = Column(Float(), nullable=False)
    y6 = Column(Float(), nullable=False)
    y7 = Column(Float(), nullable=False)
    y8 = Column(Float(), nullable=False)
    y9 = Column(Float(), nullable=False)
    y10 = Column(Float(), nullable=False)
    y11 = Column(Float(), nullable=False)
    y12 = Column(Float(), nullable=False)
    y13 = Column(Float(), nullable=False)
    y14 = Column(Float(), nullable=False)
    y15 = Column(Float(), nullable=False)
    y16 = Column(Float(), nullable=False)
    y17 = Column(Float(), nullable=False)
    y18 = Column(Float(), nullable=False)
    y19 = Column(Float(), nullable=False)
    y20 = Column(Float(), nullable=False)
    y21 = Column(Float(), nullable=False)
    y22 = Column(Float(), nullable=False)
    y23 = Column(Float(), nullable=False)
    y24 = Column(Float(), nullable=False)
    y25 = Column(Float(), nullable=False)
    y26 = Column(Float(), nullable=False)
    y27 = Column(Float(), nullable=False)
    y28 = Column(Float(), nullable=False)
    y29 = Column(Float(), nullable=False)
    y30 = Column(Float(), nullable=False)
    y31 = Column(Float(), nullable=False)
    y32 = Column(Float(), nullable=False)
    y33 = Column(Float(), nullable=False)
    y34 = Column(Float(), nullable=False)
    y35 = Column(Float(), nullable=False)
    y36 = Column(Float(), nullable=False)
    y37 = Column(Float(), nullable=False)
    y38 = Column(Float(), nullable=False)
    y39 = Column(Float(), nullable=False)
    y40 = Column(Float(), nullable=False)
    y41 = Column(Float(), nullable=False)
    y42 = Column(Float(), nullable=False)
    y43 = Column(Float(), nullable=False)
    y44 = Column(Float(), nullable=False)
    y45 = Column(Float(), nullable=False)
    y46 = Column(Float(), nullable=False)
    y47 = Column(Float(), nullable=False)
    y48 = Column(Float(), nullable=False)
    y49 = Column(Float(), nullable=False)
    y50 = Column(Float(), nullable=False)

    def __repr__(self) -> str:
        return f"<Ideal Function {self.x}>"


class Mapping(Base):
    """ Database model for mappings """
    __tablename__ = 'mappings'
    id = Column("id", Integer(), primary_key=True)
    x = Column("x (test_func)", Float(), nullable=False)
    y = Column("y (test_func)", Float(), nullable=False)
    delta = Column("Delta y (test_func)", Float(), nullable=False)
    no_of_ideal_func = Column("No of ideal func", String(50))

    def __repr__(self) -> str:
        return f"<Mapping x:{self.x} y:{self.y}>"
