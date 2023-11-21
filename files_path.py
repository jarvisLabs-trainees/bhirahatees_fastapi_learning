from fastapi import FastAPI;

app = FastAPI();

@app.get("/files/{file_path:path}")
async def file_path(file_path:str):
    return {"path" : file_path}