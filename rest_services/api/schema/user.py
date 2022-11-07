from datetime import datetime
from typing import Optional

from geoalchemy2 import WKTElement
from pydantic import (
    BaseModel,
    BaseConfig
)

from rest_services.api.crud.geocoding import Coordinates


class Userinfo(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    profession: Optional[str]
    state: Optional[str]
    city: Optional[str]
    pincode: Optional[int]
    created_on: Optional[datetime]
    updated_on: Optional[datetime]

    class Config:
        orm_mode = True


class GetUserinfo(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    profession: Optional[str]
    state: Optional[str]
    city: Optional[str]
    pincode: Optional[int]
    created_on: Optional[datetime]
    updated_on: Optional[datetime]
    location_address: Coordinates

    class Config:
        orm_mode = True


class user_create(Userinfo):
    start_location: Optional[Coordinates]


class UserInDB(Userinfo):
    """
    This schema helps to add the coordinates
    in to database using WkTElement and arbitrary
    types allowed is True it will tell you about
    the type error also.
    """
    location_address: WKTElement

    class Config(BaseConfig):
        arbitrary_types_allowed = True


class User_Loc(BaseModel):
    start_location: Optional[Coordinates]
