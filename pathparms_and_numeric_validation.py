from typing import Annotated;
from fastapi import FastAPI,Query,Path;


app = FastAPI();

@app.get("/items/{items_id}/")
async def pathparms_and_numeric_validation(item_id:Annotated[int , Path(title="Id of the Item")],name:Annotated[str | None,Query(title="item-query")] = None):
    result = {"id" : item_id};
    if name:
        result.update({"name" : name});
    return result;