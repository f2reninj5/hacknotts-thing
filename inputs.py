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


def sliders_to_bytes():
    return [slider.value for slider in sliders]


def buttons_to_bytes():
    button_bytes = []
    for i in range((len(buttons) // 8) + 1):
        byte = 0
        buttons_chunk = buttons[i * 8 : (i + 1) * 8]
        for button in buttons_chunk:
            if button.value:
                byte |= 1 << (i * 8)
                button_bytes.append(byte)
    return button_bytes
