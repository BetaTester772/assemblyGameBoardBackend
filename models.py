from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from database import Base


class Game1(Base):
    __tablename__ = "game1"
    
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    score = Column(Integer, nullable=True)
    session_id = Column(Integer, nullable=True)


class Game2(Base):
    __tablename__ = "game2"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    score = Column(Integer, nullable=True)
    session_id = Column(Integer, nullable=True)


class Game3(Base):
    __tablename__ = "game3"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=True)
    name = Column(String, nullable=True)
    score = Column(Integer, nullable=True)
    session_id = Column(Integer, nullable=True)
