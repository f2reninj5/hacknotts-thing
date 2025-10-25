import struct

from inputs import buttons_to_bytes, sliders_to_bytes
import usb_cdc
import time

usb_cdc.enable(console=True, data=True)
data = usb_cdc.data

while True:
    button_bytes = buttons_to_bytes()
    slider_bytes = sliders_to_bytes()
    struct_format = "<" + "B" * len(button_bytes) + "H" * len(slider_bytes)
    payload = struct.pack(struct_format, *button_bytes, *slider_bytes)
    usb_cdc.data.write(payload)
    time.sleep(0.1)
