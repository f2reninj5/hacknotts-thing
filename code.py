from inputs import buttons, sliders
import time

while True:
    for i, button in enumerate(buttons):
        print(f"Button {i} value: {button.value}")
    for i, slider in enumerate(sliders):
        print(f"Slider {i} value: {slider.value}")
    time.sleep(1)
