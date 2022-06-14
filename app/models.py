from sqlalchemy import Column, Integer, String

from .database import Base


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    isbn = Column(String(50))
    title = Column(String(150))
    description = Column(String(250))
    author = Column(String(150))