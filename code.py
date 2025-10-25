import usb_cdc

usb_cdc.enable(console=False, data=True)

import struct
import time
from inputs import buttons_to_bytes, sliders_to_bytes

data = usb_cdc.data

while True:
    if data.in_waiting > 0:
        msg = data.read(data.in_waiting)
        if msg.decode() == "go":
            break

while True:
    button_bytes = buttons_to_bytes()
    slider_bytes = sliders_to_bytes()
    struct_format = "<" + "B" * len(button_bytes) + "H" * len(slider_bytes)
    payload = struct.pack(struct_format, *button_bytes, *slider_bytes)
    usb_cdc.data.write(payload)
    time.sleep(0.1)
