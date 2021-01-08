# Write your code here :-)
import board
from digitalio import DigitalInOut, Direction

sw1 = DigitalInOut(board.D2)
sw2 = DigitalInOut(board.D0)
led = DigitalInOut(board.D13)
sw1.direction = Direction.INPUT
sw2.direction = Direction.INPUT
led.direction = Direction.OUTPUT

while True:
    if not sw1:
        led.value = True
        pass
    if not sw2:
        led.value = False