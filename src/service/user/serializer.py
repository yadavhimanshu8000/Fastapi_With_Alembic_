from pydantic import BaseModel , EmailStr
from typing import Optional
from datetime import date


class Userserilaizerresponse(BaseModel):
    user_id: int
    user_name: str
    user_email: str
    gender: str
  
  
class Userserilaizerrequest(BaseModel):
    user_name : str
    description: str
    user_email:EmailStr
    dob: Optional[date] = None
    gender: str


class User_one(Userserilaizerresponse):
    user_id: int


    class Config:
        from_attributes = True 
          


