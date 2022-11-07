from fastapi import FastAPI

from .api import main

app = FastAPI(title="East vantage assessment",
              description="This small project is all about the "
                          "apis which creates the user,update,get,"
                          "delete the user."
              )
app.include_router(main.app)
