from fastapi import FastAPI;
import requests;
from pydantic import BaseModel;

class Numbers(BaseModel):
    num1:int;
    num2:int;

app = FastAPI();

@app.post("/sum")
async def sumVtwo(numbers:Numbers):
    response = requests.post(url="https://a61d8c1945db92dedc753e9463264fc0.notebooksb.jarvislabs.net/sum",data=numbers.json());
    return response.json();