import serial
import struct

if __name__ == "__main__":
    ser = serial.Serial("COM3", 115200, timeout=1)

    ser.write("go".encode())

    while True:
        data = ser.read(9)
        values = struct.unpack("<BBBHHH", data)
        print(values)
