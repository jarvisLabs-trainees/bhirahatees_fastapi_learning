from enum import Enum;
from fastapi import FastAPI;

app = FastAPI();

class values(str,Enum):
    boss = "Bhirahatees";
    soldier = "Arun";

        
    

@app.get("/{name}")
async def root(name : values):
    if name is values.boss:
        return {"Message" : "Hello Boss"};
    elif name is values.soldier:
        return {"Message" : "Hello Commander"}
        
@app.get("/files/{file_path:path}")
async def file_path(file_path:str):
    return {"path" : file_path}