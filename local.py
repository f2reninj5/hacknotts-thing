import serial
import serial.tools.list_ports
import struct


def find_pico():
    for port in serial.tools.list_ports.comports():
        if port.vid == 0x2E8A:
            return port.device
    return None


NUM_BUTTONS = 3
NUM_SLIDERS = 3

NUM_BUTTON_BYTES = (NUM_BUTTONS // 8) + 1
NUM_SLIDER_BYTES = NUM_SLIDERS * 2
STRUCT_SIZE = NUM_BUTTON_BYTES + NUM_SLIDER_BYTES
struct_format = "<" + "B" * NUM_BUTTON_BYTES + "H" * NUM_SLIDER_BYTES

if __name__ == "__main__":
    ser = serial.Serial(find_pico(), 115200, timeout=1)

    ser.write("go".encode())

    while True:
        data = ser.read(STRUCT_SIZE)
        values = struct.unpack(struct_format, data)
        print(values)
