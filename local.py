import serial
import struct
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

ser = serial.Serial("COM3", 115200, timeout=1)

ser.write("go".encode())


@app.websocket("/pico")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = ser.read(9)
            values = struct.unpack("<BBBHHH", data)
            await websocket.send_json({data: list(values)})
    except WebSocketDisconnect:
        print("Disconnected")
