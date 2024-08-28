from sqlalchemy import Column, Integer, Text, create_engine, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, nullable=False)


class Survey(Base):
    __tablename__ = 'surveys'

    survey_id = Column(Integer, nullable=False)
    question_id = Column(Integer, nullable=False)
    question = Column(Text, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('survey_id', 'question_id'),
    )


class Response(Base):
    __tablename__ = 'responses'

    user_id = Column(Integer, nullable=False)
    survey_id = Column(Integer, nullable=False)
    question_id = Column(Integer, nullable=False)
    response = Column(Text, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'survey_id', 'question_id'),
    )


DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
