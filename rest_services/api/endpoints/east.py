"""
This file contains Api services
which helps to interact with the
database and usefully business logics.
"""
import logging
from typing import List

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy import func
from sqlalchemy.orm import Session

from ..crud.geocoding import get_geom_from_coordinates, get_coordinates_from_geom
from ..model.east import User
from ..schema.user import (
    UserInDB,
    GetUserinfo,
    user_create,
    User_Loc,
    Userinfo
)
from ..utils.db import get_db

app = APIRouter()


@app.post("/create_user")
async def create_user(userinfo: user_create, db: Session = Depends(get_db)):
    """
    This is post request api as software methodology this post
    HTTP protocol is used to add the data in to database.
    """
    logging.info(f"User entry data {userinfo}")
    print(userinfo)
    coordinates_from_geom = get_geom_from_coordinates(userinfo.start_location)
    user_obj = UserInDB(**userinfo.dict(), location_address=coordinates_from_geom)
    print(f"user_object data {user_obj}")
    user_data = User(**user_obj.dict())
    db.add(user_data)
    db.commit()
    db.close()
    return HTMLResponse(
        content="Successfully added the user info data",
        status_code=201
    )


@app.get("/get/users/info", response_model=List[GetUserinfo])
async def get_user_details(db: Session = Depends(get_db)):
    """
    Get the all the user objects from the db.
    """
    user_obj = db.query(User).all()
    for user in user_obj:
        user.location_address = get_coordinates_from_geom(user.location_address)
    return user_obj


@app.get("/get/user", response_model=GetUserinfo)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    This rest api service is get particular user
    data from the database.
    """
    user_obj = db.query(User).filter(User.user_id == user_id).first()
    if user_obj:
        user_obj.location_address = get_coordinates_from_geom(user_obj.location_address)
        return user_obj
    else:
        return HTMLResponse(
            content=f"user does not exist with given id {user_id}",
            status_code=404
        )


@app.delete("/remove/user")
async def remove_user_info(user_id: int, db: Session = Depends(get_db)):
    user_obj = db.query(User).filter(User.user_id == user_id).first()
    if user_obj:
        db.delete(user_obj)
        db.commit()
        db.close()
        return HTMLResponse(
            content="Successfully removed the given user",
            status_code=200
        )
    else:
        return HTMLResponse(
            content="Given user info is does not exist",
            status_code=404
        )


@app.put("/update/user/info")
async def user_info_update(user_id: int, userinfo: user_create, db: Session = Depends(get_db)):
    """
    This HTTps method is used to update given id
    record
    """
    user_obj = db.query(User).filter(User.user_id == user_id).first()
    if user_obj:
        coordinates_from_geom = get_geom_from_coordinates(userinfo.start_location)
        user_obj.location_address = coordinates_from_geom
        user_obj.first_name = userinfo.first_name
        user_obj.last_name = userinfo.last_name
        user_obj.profession = userinfo.profession
        user_obj.state = userinfo.state
        user_obj.city = userinfo.city
        user_obj.pincode = userinfo.pincode
        user_obj.update_on = userinfo.updated_on
        db.add(user_obj)
        db.commit()
        return HTMLResponse(
            content="Successfully update the user data",
            status_code=200
        )
    else:
        return HTMLResponse(
            content="User does not exist",
            status_code=404
        )


@app.post("/get/nearest", response_model=List[Userinfo])
async def get_nearest_user(user_location: User_Loc, db: Session = Depends(get_db)):
    """
    This method is used to get the
    nearest location user info
    from the db.
    """
    str_geom = 'SRID=4326;' + str(get_geom_from_coordinates(user_location.start_location))
    user_obj = db.query(User).filter((func.ST_Distance(func.ST_Transform(User.location_address, 3857),
                                                       func.ST_Transform(str_geom,
                                                                         3857)) / 1000) < 1000).all()
    return user_obj
