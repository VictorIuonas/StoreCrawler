from sqlalchemy import Column, Integer, String

from DAL.db_init import Base


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    Currency = Column(String(10), nullable=False)
    Description = Column(String(250), nullable=True)
    # image string array
