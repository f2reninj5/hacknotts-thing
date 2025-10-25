import usb_cdc
import struct
import time
from inputs import get_button_bytes, get_slider_bytes

data = usb_cdc.data

while True:
    if data.in_waiting > 0:
        msg = data.read(data.in_waiting).decode().strip()
        if msg == "go":
            break
    time.sleep(0.01)

while True:
    button_bytes = get_button_bytes()
    slider_bytes = get_slider_bytes()
    payload = struct.pack("<BBBHHH", *button_bytes, *slider_bytes)
    data.write(payload)
    time.sleep(0.01)
