import json
import websockets
import itertools

class HAWebSocket:
    def __init__(self, url, token):
        self.url = url.replace("http", "ws") + "/api/websocket"
        self.token = token
        self._id = itertools.count(1)

    async def call(self, command, **kwargs):
        async with websockets.connect(self.url) as ws:
            # 1. Auth required
            msg = json.loads(await ws.recv())
            if msg["type"] != "auth_required":
                raise Exception("Unexpected auth message")

            await ws.send(json.dumps({
                "type": "auth",
                "access_token": self.token
            }))

            msg = json.loads(await ws.recv())
            if msg["type"] != "auth_ok":
                raise Exception("Auth failed")

            # 2. Send command
            call_id = next(self._id)
            await ws.send(json.dumps({
                "id": call_id,
                "type": command,
                **kwargs
            }))

            # 3. Wait for result
            while True:
                response = json.loads(await ws.recv())
                if response.get("id") == call_id:
                    if not response.get("success"):
                        raise Exception(response)
                    return response["result"]
