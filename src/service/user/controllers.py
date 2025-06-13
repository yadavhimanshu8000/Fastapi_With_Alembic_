from src.service.user.models import User
from src.service.user.serializer import Userserilaizerrequest
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from sqlalchemy.future import select



async def Createuser(user: Userserilaizerrequest, db: AsyncSession):
    result = await db.execute(select(User).where(User.user_email == user.user_email))
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )
    
    new_user = User(
        user_name = user.user_name,
        description = user.description,
        user_email = user.user_email,
        dob = user.dob,
        gender = user.gender
        
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user



async def Getuser(db: AsyncSession, user_id : int):
    result=  await db.execute(select(User).where(User.user_id == user_id))
    user = result.scalar_one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    return user



async def Getallusers(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users



async def Updateuser(db: AsyncSession, user_id: int, user: Userserilaizerrequest):
    result = await db.execute(select(User).where(User.user_id == user_id))
    db_user = result.scalar_one_or_none()

    if db_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
 

    db_user.user_name = user.user_name
    db_user.description = user.description
    db_user.user_email = user.user_email
    db_user.dob = user.dob
    db_user.gender = user.gender

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user



async def Deleteuser(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.user_id == user_id))
    db_user = result.scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail='User Not Found')
    
    await db.delete(db_user)
    await db.commit()
    # await db.refresh(db_user)
    return db_user










    
