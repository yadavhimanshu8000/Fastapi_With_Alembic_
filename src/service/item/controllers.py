from src.service.item.models import Item
from src.service.item.serializer import Itemserilaizerrequest
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.future import select
from src.service.user.models import *



async def Createitem(item: Itemserilaizerrequest, db: AsyncSession):
    result = await db.execute(select(User).where(User.user_id == item.owner_id))
    existing_user = result.scalar_one_or_none()
    
    if existing_user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = 'Owner_id Not Found'
        )
   
    product = Item(
        item_name = item.item_name,
        price = item.price,
        owner_id = item.owner_id       
    )
    
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product



async def Getitem(db: AsyncSession, item_id : int):
    result=  await db.execute(select(Item).where(Item.item_id == item_id))
    item = result.scalar_one_or_none()
    
    if item is None:
        raise HTTPException(status_code=404, detail='Item Not Found')
    return item



async def Getallitem(db: AsyncSession):
    result = await db.execute(select(Item))
    item = result.scalars().all()
    return item



async def Updateitem(db: AsyncSession, item_id: int, item: Itemserilaizerrequest):
    result = await db.execute(select(Item).where(Item.item_id == item_id))
    db_item = result.scalar_one_or_none()

    if db_item is None:
        raise HTTPException(status_code=404, detail='Item Not Found')
 
    db_item.item_name = item.item_name
    db_item.price = item.price
    db_item.owner_id = item.owner_id
   

    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item



async def Deleteitem(db: AsyncSession, item_id: int):
    result = await db.execute(select(Item).where(Item.item_id == item_id))
    db_item = result.scalar_one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail='Item Not Found')
    
    await db.delete(db_item)
    await db.commit()
    # await db.refresh(db_user)
    return db_item
