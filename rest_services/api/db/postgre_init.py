"""
Here the all the mess is going on about
the db connection and creating the engine
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .creds import dbuser, dbhost, dbpass, dbname

print(dbhost)

SQLALCHEMY_DATABASE_URL = "postgresql://" + \
                          dbuser + ":" + dbpass + "@" + dbhost + "/" + dbname
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
