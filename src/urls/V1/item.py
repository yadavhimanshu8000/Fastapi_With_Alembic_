from fastapi import APIRouter,Depends,Request
from src.service.item.serializer import *
from src.database.db import get_db, AsyncSession
from src.service.item.controllers import *
from typing import List
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/V1/item")


@router.post("/item_create/")
async def item_api_user(item: Itemserilaizerrequest , db: AsyncSession = Depends(get_db)):
    await Createitem(item,db)
    return {"message": "Item Created Successfully"}



@router.get("/get_item/{item_id}",response_model=Item_one)
async def get_item_api(item_id: int, db: AsyncSession = Depends(get_db)):
    store = await Getitem(db, item_id)
    return store



@router.get("/get_item_all/",response_model=List[Itemserilaizerresponse])
async def get_item_all_api(db: AsyncSession = Depends(get_db)):
    store = await Getallitem(db)
    return store



@router.put('/update_item/{item_id}', response_model=Itemserilaizerrequest)
async def update_item_api(item_id: int, item: Itemserilaizerrequest, db: AsyncSession = Depends(get_db)):
    updated_item = await Updateitem(db, item_id, item)
    return updated_item



@router.delete('/delete_item/{item_id}')
async def delete_item_api(item_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await Deleteitem(db, item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return JSONResponse(status_code=200, content={"message": "Item Deleted Successfully"})

