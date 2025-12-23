import os
MUSIC_ASSISTANT_BASE_URL = "http://addon_music_assistant:9095"
# If MA runs elsewhere, change this

# Long-lived access token from Home Assistant
HA_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJiN2RiMGYwZTY2YTk0ODUxYjIxNjk3ZGE1MjEwOTEyOCIsImlhdCI6MTc2NjQ4NjE0OCwiZXhwIjoyMDgxODQ2MTQ4fQ.qgUvC5dttbmtnvqdgVcDmuDStKdHWv3hvivJokTqS0w"

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
