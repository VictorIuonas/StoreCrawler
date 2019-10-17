from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from DAL.db_init import Base

session_engine = create_engine('sqlite:///products-db')
Base.metadata.bind = session_engine

DBSession = sessionmaker(bind=session_engine)
session = DBSession()
