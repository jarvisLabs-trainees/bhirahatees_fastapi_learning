from typing import Annotated;
from fastapi import FastAPI , Query;

app = FastAPI();

@app.get("/items/queries/{id}")
async def create_items(id:int , name : Annotated[str | None , Query(min_length=3,max_length=13,regex="^[A-Za-z]")]):
    return {"id":id , "name" : name};
