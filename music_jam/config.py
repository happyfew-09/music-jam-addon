import os
MUSIC_ASSISTANT_BASE_URL = "http://music-assistant:9095"
# If MA runs elsewhere, change this

# Long-lived access token from Home Assistant
HA_TOKEN = os.environ.get("SUPERVISOR_TOKEN")

ZONES = {
    "living_room": {
        "name": "Living Room",
        "player_id": "media_player.intense_soundbar_2",
        "max_queue": 50,
    },
    "bedroom": {
        "name": "Bedroom PC",
        "player_id": "media_player.happyfew09_pc",
        "max_queue": 30,
    },
    "phone": {
        "name": "Phone / Bluetooth",
        "player_id": "media_player.squeezeplay_b5_5b_42_15_43_cd",
        "max_queue": 20,
    },
}
