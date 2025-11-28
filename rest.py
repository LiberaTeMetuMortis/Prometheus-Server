from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json

app = FastAPI(title="Prometheus Rover Dashboard API")

# CORS (Frontend erişimi için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

robot_state = {
    "task_id": None,
    "status": "OFFLINE",
    "progress": 0,
    "pos": {"x": 0.0, "y": 0.0, "theta": 0.0},
    "type": "none"
}

@app.get("/")
def read_root():
    return {"message": "Prometheus Dashboard API Çalışıyor! 🚀"}

@app.get("/api/status")
def get_status():
    return robot_state

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🔌 Robot Bağlandı!")
    try:
        while True:
            data = await websocket.receive_json()

            if "pos" in data and isinstance(data["pos"], (list, tuple)):
                raw_pos = data["pos"]
                if len(raw_pos) >= 3:
                    data["pos"] = {
                        "x": raw_pos[0],
                        "y": raw_pos[1],
                        "theta": raw_pos[2]
                    }

            global robot_state
            robot_state = data
            print(f"📡 Durum Güncellendi: {robot_state}")

    except WebSocketDisconnect:
        print("❌ Robot Bağlantısı Koptu.")
        robot_state["status"] = "DISCONNECTED"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)