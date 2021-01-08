# https://makeandymake.github.io/2020/05/02/seeeduino-xiao-circuitpython-usb-hid-macro-keypad.html


import digitalio

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import board

import usb_hid


sw1 = digitalio.DigitalInOut(board.D4)
sw2 = digitalio.DigitalInOut(board.D0)
led = digitalio.DigitalInOut(board.D13)
sw1.direction = digitalio.Direction.INPUT
sw2.direction = digitalio.Direction.INPUT
sw1.pull = digitalio.Pull.UP
sw2.pull = digitalio.Pull.UP
led.direction = digitalio.Direction.OUTPUT
led.value = True

for x in range(0, 5):

    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.2)



def open_app(app):
	kbd.send(Keycode.COMMAND, Keycode.SPACE)
	time.sleep(0.2)
	layout.write(app)
	time.sleep(0.2)
	kbd.send(Keycode.ENTER)


while True:

    if not sw1.value:

    	# open Chrome and go to gmail
    	led.value = False # led on
    	open_app("Chrome.app")
        time.sleep(0.5)
        kbd.send(Keycode.COMMAND, Keycode.T)
        time.sleep(0.2)
        layout.write('https://mail.google.com')
        time.sleep(0.5)
        kbd.send(Keycode.ENTER)
        time.sleep(0.5)
        led.value = True # led off

    if not sw2.value:

    	# open finder
    	led.value = False # led on
    	open_app("~")
        led.value = True # led off
        time.sleep(0.5)  # debounce delay

