from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    description: str | None = None
    tax: float | None = None

@app.post("/items/{item_id}/")
async def create_item_with_id(item_id: int, item:Item ,query: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if query:
        result.update({"text": query})  
    return result
