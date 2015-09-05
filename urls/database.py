from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from urls import app

engine = create_engine(app.config["DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True)
    url = Column(Text)
    savedate = Column(DateTime, default=datetime.datetime.now)
    user= Column(Text)



Base.metadata.create_all(engine)
