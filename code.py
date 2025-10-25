import board
import digitalio
import analogio
import time

buttons = [
    digitalio.DigitalInOut(pin)
    for pin in [
        board.GP16,
        board.GP17,
        board.GP18,
    ]
]

for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.DOWN

sliders = [
    analogio.AnalogIn(pin)
    for pin in [
        board.GP26_A0,
        board.GP27_A1,
        board.GP28_A2,
    ]
]

while True:
    for i, button in enumerate(buttons):
        print(f"Button {i} value: {button.value}")
    for i, slider in enumerate(sliders):
        print(f"Slider {i} value: {slider.value}")
    time.sleep(1)
