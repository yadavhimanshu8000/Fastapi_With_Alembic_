from fastapi import FastAPI
from src.database.db import engine
from src.service.user import models
from src.service.item import models
from src.urls.V1 import(
    item,
    user
)


app = FastAPI(
        title="User_Details",
        description="Fastapi",
        version="1.0.0",
        contact={
        "name": "Himanshu",
        "url": "https://github.com/yadavhimanshu8000",
        "email": "singhhimanshu8000@gmail.com"
        },
        license_info={
            "name": "Softedge",
            "url": "https://softedge.in/",
        },
        terms_of_service="https://www.example.com/terms",
        docs_url='/docs',
    )

# Create tables asynchronously
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Run this at startup
@app.on_event("startup")
async def on_startup():
    await init_models()


@app.get("/")
async def Root():
    return {"message": "user_item"}


app.include_router(user.router,tags=["Users"])
app.include_router(item.router,tags=["Items"])

