from pydantic import BaseModel , EmailStr
from typing import Optional
from datetime import date
from src.service.user.models import *


class Itemserilaizerresponse(BaseModel):
    item_id: int
    item_name: str
    price: int
    owner_id: int
    
    
class Itemserilaizerrequest(BaseModel):
    item_name : str
    price: int
    owner_id: int
    
   
class Item_one(Itemserilaizerresponse):
    item_id: int
    
    
    class Config:
        from_attributes = True 
          

