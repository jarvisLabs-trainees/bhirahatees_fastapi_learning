from fastapi import FastAPI

app = FastAPI()

@app.get("/profile/")
async def profile(firstname:str, lastname:str | None = None):
    if lastname is not None:
        return {"name" : firstname +" "+ lastname,"message":True};
    else:
        return {"name" : firstname,"message":False}
       
