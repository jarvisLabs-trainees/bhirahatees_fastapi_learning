from text_to_speech import text_to_speech;
from fastapi import FastAPI;
from pydantic import BaseModel;

app = FastAPI();

class sentence(BaseModel):
    name:str;

@app.post("/speaker")
async def speaker_api(sentence:sentence):
    text_to_speech("hello "+ sentence.name);
    return "Success";

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=5000);