import board, digitalio, usb_hid, time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Set the pin object representing an I/O pin to be assigned to the button variable
button = digitalio.DigitalInOut(board.GP10)
# Configure the button to be an input
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Create an instance of the Keyboard class that contains the USB HID devices
keyboard = Keyboard(usb_hid.devices)
# Configure object that can send keyboard events
layout = KeyboardLayoutUS(keyboard)

while True:
    button_pressed = button.value
    
    with open('./text_to_paste.txt', 'r') as file:
        text_to_paste = file.read().strip()

    if button_pressed:
        layout.write(text_to_paste)
        time.sleep(0.5)
    else:
        continue