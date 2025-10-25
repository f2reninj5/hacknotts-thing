import board
import digitalio
import analogio

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
