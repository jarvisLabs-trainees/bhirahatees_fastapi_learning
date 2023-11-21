from fastapi import FastAPI;

app = FastAPI();

@app.get("/myname")
async def say_my_name():
    return "Hello Bhirahatees";

@app.get("/{name}")
async def say_my_name(name:str):
    return "Hello " + name;