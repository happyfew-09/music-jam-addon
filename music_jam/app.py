from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import requests
import traceback
from config import MUSIC_ASSISTANT_BASE_URL, HA_TOKEN, ZONES

app = FastAPI()

if not HA_TOKEN:
    raise RuntimeError("SUPERVISOR_TOKEN not found")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def index():
    with open("static/index.html") as f:
        return f.read()


@app.get("/zones")
def get_zones():
    return {
        zone_id: {"name": z["name"]}
        for zone_id, z in ZONES.items()
    }


@app.get("/search")
def search(q: str):
    print(f"Search request received: {q}")

    r = requests.post(
        f"{MUSIC_ASSISTANT_BASE_URL}/api/media/search",
        json={
            "query": q,
            "media_types": ["track"],
            "limit": 10
        },
        headers={
            "Authorization": f"Bearer {HA_TOKEN}",
            "Content-Type": "application/json"
        },
        timeout=10,
    )

    r.raise_for_status()
    return r.json()



@app.post("/zones/{zone_id}/queue")
def add_to_queue(zone_id: str, track_uri: str):
    if zone_id not in ZONES:
        raise HTTPException(404, "Unknown zone")

    player_id = ZONES[zone_id]["player_id"]

    # Add track to queue
    r = requests.post(
        f"{MUSIC_ASSISTANT_BASE_URL}/players/{player_id}/queue",
        json={"uri": track_uri},
        headers=HEADERS,
        timeout=10,
    )
    if not r.ok:
        raise HTTPException(500, "Failed to add to queue")

    # Start playback if idle
    requests.post(
        f"{MUSIC_ASSISTANT_BASE_URL}/players/{player_id}/play",
        headers=HEADERS,
        timeout=5,
    )

    return {"status": "ok"}
