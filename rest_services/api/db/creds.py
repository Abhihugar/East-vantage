"""
This file gets the db creds info
from the .env or dev env file from your
directory.
"""
import os

import dotenv

try:
    dotenv.load_dotenv("./rest_services/dev.env")
except Exception as e:
    print(e)

dbhost = os.environ.get("DBHOST")
dbuser = os.environ.get("DBUSER")
dbpass = os.environ.get("DBPASS")
dbname = os.environ.get("DBNAME")
