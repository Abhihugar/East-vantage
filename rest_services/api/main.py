
from fastapi import APIRouter

from .db.postgre_init import Base, engine
from .endpoints import east

app = APIRouter()

# Initializing DataLayer
'''All models should be imported'''
Base.metadata.create_all(bind=engine)

app.include_router(east.app, tags=["East"])


@app.get("/")
async def welcome():
    return 'Welcome to East vantage'
