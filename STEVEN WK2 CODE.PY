import board
import time
from digitalio import DigitalInOut, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1
# create a color as a tuple value
x_green = 0x2c9c18
s_greenblue = 0x2994f
y_blue = 0x3176BD

# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)

button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)


# A variable to track the LED led state
led_state = True

while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_a_read = button_a.value
    button_b_read = button_b.value
    

    # set variables based on the value of your inputs
    if button_a_read is True and button_b_read is True:
        pixels.fill(y_blue)
    elif button_a_read is True:
        pixels.fill(x_green)
    elif button_b_read is True:
        pixels.fill(s_greenblue)

    else:
        led_state = False
        pixels.fill(0)

    time.sleep(0.1)
