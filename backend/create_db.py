from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.model import Base, User, Survey, Response

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

users = [
    User(user_id=1, survey_id=101),
    User(user_id=2, survey_id=101),
    User(user_id=3, survey_id=102),
    User(user_id=4, survey_id=102),
    User(user_id=5, survey_id=103)
]

surveys = [
    Survey(survey_id=101, question_id=1,
           question="How satisfied are you with our service?"),
    Survey(survey_id=101, question_id=2,
           question="Would you recommend our service to others?"),
    Survey(survey_id=102, question_id=3,
           question="How easy was it to use the product?"),
    Survey(survey_id=102, question_id=4,
           question="How likely are you to use the product again?")
]

responses = [
    Response(user_id=1, survey_id=101, question_id=1,
             response="Very satisfied"),
    Response(user_id=1, survey_id=101, question_id=2, response="Yes"),
    Response(user_id=2, survey_id=101, question_id=1, response="Satisfied"),
    Response(user_id=2, survey_id=101, question_id=2, response="Maybe"),
    Response(user_id=3, survey_id=102, question_id=3, response="Easy"),
    Response(user_id=3, survey_id=102, question_id=4, response="Very likely"),
    Response(user_id=4, survey_id=102, question_id=3, response="Difficult"),
    Response(user_id=4, survey_id=102, question_id=4, response="Unlikely"),
    Response(user_id=5, survey_id=103, question_id=1, response="Neutral")
]

db.add_all(users + surveys + responses)
db.commit()

print("Database created and initial data inserted.")
