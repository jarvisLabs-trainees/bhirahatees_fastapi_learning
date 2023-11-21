from fastapi import FastAPI;

app = FastAPI();

@app.get("/")
async def root():
    return {"message": "Hello World", "first-name" :"Bhirahatees","last-name":"Periyasamy"};

