from src.database.db import Base
from sqlalchemy import Integer , Column , String , ForeignKey
from src.service.user.models import *

class Item(Base):
    __tablename__ = "item"
    
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    owner_id = Column(Integer,  ForeignKey('user.user_id'), nullable=False)
    
