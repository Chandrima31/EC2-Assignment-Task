from fastapi import FastAPI
from databases import Database


app = FastAPI()

database = Database("sqlite:///demo.db")


@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()


@app.post("/titanic")
async def fetch_data(id: int):
    query = "SELECT * FROM titanic_data WHERE PassengerId={}".format(str(id))
    results = await database.fetch_all(query=query)

    return  results