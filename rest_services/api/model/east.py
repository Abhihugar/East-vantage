from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, DateTime

from ..db.postgre_init import Base


class User(Base):
    """
    This user model stores the basic
    information about the user along
    with coordinates.
    """
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    profession = Column(String)
    state = Column(String)
    city = Column(String)
    pincode = Column(Integer)
    created_on = Column(DateTime)
    updated_on = Column(DateTime)
    location_address = Column(Geometry('POINT', 4326, from_text='ST_GeomFromEWKT'))
