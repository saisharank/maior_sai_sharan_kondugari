from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    type = Column(String(10))
    joke = Column(String(255), nullable=True)
    setup = Column(String(255), nullable=True)
    delivery = Column(String(255), nullable=True)
    flags_nsfw = Column(Boolean)
    flags_political = Column(Boolean)
    flags_sexist = Column(Boolean)
    safe = Column(Boolean)
    lang = Column(String(10))
