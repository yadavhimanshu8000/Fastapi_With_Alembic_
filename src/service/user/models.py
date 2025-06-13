from src.database.db import Base
from sqlalchemy import Integer , Column , String ,Date



class User(Base):
    __tablename__ = "user"
    
    user_id = Column(Integer, primary_key= True, index= True)
    user_name = Column(String, nullable= False)
    description = Column(String, nullable= True)
    user_email = Column(String, nullable=False, unique=True)
    dob = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    