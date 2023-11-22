from fastapi import FastAPI;
from pydantic import BaseModel;
import replicate;

app = FastAPI();

class PromptClass(BaseModel):
    prompt_str : str;

@app.post("/model/sdxl")
async def get_image(prompt : PromptClass):
    output = replicate.run(
        "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
        input={"prompt" : prompt.prompt_str},
    );
    return {"image" :output};