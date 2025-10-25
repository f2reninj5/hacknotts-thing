import board
import digitalio
import time

buttons = [digitalio.DigitalInOut(pin) for pin in [
    board.GP16,
    board.GP17,
    board.GP18,
]]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN

while True:
    for i, button in enumerate(buttons):
        print(f"Button {i} value: {button.value}")
    time.sleep(0.1)
