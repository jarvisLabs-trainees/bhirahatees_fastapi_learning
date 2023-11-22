from fastapi import FastAPI;
import requests;


app = FastAPI();

@app.get("/hello")
async def hello_world():
    result = requests.get("https://a61d8c1945db92dedc753e9463264fc0.notebooksb.jarvislabs.net");
    return result.json();