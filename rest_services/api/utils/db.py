from ..db.postgre_init import SessionLocal


def get_db():
    """
    This is small db utility method
    which helps write the query as well
    as yield the object from the db.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
