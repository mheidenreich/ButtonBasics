#!/usr/bin/python3

"""
    Program: GPIO Button Basics (buttons.py)
    Author:  M. Heidenreich, (c) 2020-2022

    Description: This code is provided in support of the following YouTube tutorial:
                 https://youtu.be/YICzRCAY73Y

    This tutorial is an introduction to how to use buttons with the Raspberry Pi.

    THIS SOFTWARE AND LINKED VIDEO TOTORIAL ARE PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS
    ALL WARRANTIES INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
    IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES
    OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
    NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from signal import pause
from time import sleep
from gpiozero import LED, Button

blink_on = False
interval = 0.5

button = Button(21)
led1 = LED(26)
led2 = LED(19)

def go_blink():
    global blink_on

    if blink_on:
        led1.off()
        led2.off()
    else:
        led1.blink(interval, interval)
        sleep(interval)
        led2.blink(interval, interval)

    blink_on = not blink_on

try:
    button.when_pressed = go_blink
    pause()

except KeyboardInterrupt:
    pass

finally:
    led1.close()
    led2.close()
