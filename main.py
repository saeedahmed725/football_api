# main.py
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from premier_league.premier_league_scraper import getstandings 
import io

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Football API!"}

@app.get("/standings")
async def standings():
    json_data = getstandings()
    return StreamingResponse(io.StringIO(json_data), media_type="application/json", headers={"Content-Disposition": "attachment; filename=premier_league_standings.json"})
