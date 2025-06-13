from fastapi import APIRouter,Depends,Request
from src.service.user.serializer import *
from src.database.db import get_db
from src.service.user.controllers import *
from typing import List
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/V1/user")



@router.post("/user_create/")
async def create_user_api(user: Userserilaizerrequest , db: AsyncSession = Depends(get_db)):
    await Createuser(user,db)
    return {"message": "User Created Successfully"}



@router.get("/get_user/{user_id}",response_model=User_one)
async def get_user_api(user_id: int, db: AsyncSession = Depends(get_db)):
    store = await Getuser(db, user_id)
    return store



@router.get("/get_user_all/",response_model=List[Userserilaizerresponse])
async def get_user_all_api(db: AsyncSession = Depends(get_db)):
    store = await Getallusers(db)
    return store



@router.put('/update_user/{user_id}', response_model=Userserilaizerrequest)
async def update_user_api(user_id: int, user: Userserilaizerrequest, db: AsyncSession = Depends(get_db)):
    updated_user = await Updateuser(db, user_id, user)
    return updated_user



@router.delete('/delete_user/{user_id}',response_model=Userserilaizerrequest)
async def delete_user_api(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await Deleteuser(db,user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User Not Found")
    
    return JSONResponse(status_code=200, content={"message": "User Delete Successfully"})

