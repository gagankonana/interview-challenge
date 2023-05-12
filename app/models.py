from sqlalchemy import Column, Integer, String, DateTime, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import sessionmaker
import settings


Base = declarative_base()

SQLALCHEMY_DATABASE_URL = settings.DB_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class BusinessSymptomData(Base):
    __tablename__ = "business_symptom_data"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    business_id = Column(Integer, nullable=False)
    business_name = Column(String(30),  nullable=False)
    symptom_code = Column(String(30),  nullable=False)
    symptom_name = Column(String(30),  nullable=False)
    symptom_diagnostic = Column(Boolean,  nullable=False)
