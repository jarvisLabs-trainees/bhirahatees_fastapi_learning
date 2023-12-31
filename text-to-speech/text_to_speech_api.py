from text_to_speech import text_to_speech;
from fastapi import FastAPI;
from pydantic import BaseModel;

app = FastAPI();

class sentence(BaseModel):
    line:str;

@app.post("/speaker")
async def speaker_api(sentence:sentence):
    text_to_speech(sentence.line);
    return "Success";

