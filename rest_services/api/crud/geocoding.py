from geoalchemy2 import WKTElement
from geoalchemy2.shape import to_shape
from pydantic import BaseModel, validator


class Coordinates(BaseModel):
    """
    This method is all about the
    coordinates which help us to take
    lat long from front end .
    """
    lat: float = 0
    lng: float = 0

    @validator('lat')
    def lat_within_range(cls, v):
        """
        This method is used to check the
        given lat is present within range
        or not or else it will raise the
        validation error.
        """
        if not -90 <= v <= 90:
            raise ValueError('Latitude outside allowed range')
        return v

    @validator('lng')
    def lng_within_range(cls, v):
        """
        This method is used to check the
        given long value is within range
        or not or else this also raise the
        validation error.
        """
        if not -180 <= v <= 180:
            raise ValueError('Longitude outside allowed range')
        return v


def get_geom_from_coordinates(coordinates: Coordinates):
    """
    This method returns the tuple of lat long which
    helps to store the lat long in a single field.
    and also for conversations
    """
    geom_wkte = WKTElement(
        f"Point ({coordinates.lng} {coordinates.lat})",
        srid=4326, extended=True)
    return geom_wkte


# sending the output with lat lng
def get_coordinates_from_geom(geom: WKTElement):
    """
    This method is called only when you want to get the
    lat long from the db.
    """
    shply_geom = to_shape(geom)
    coordinates = Coordinates(lng=shply_geom.x, lat=shply_geom.y)
    return coordinates
