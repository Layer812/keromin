import time
import board
from rainbowio import colorwheel
import neopixel

import time
import random
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff
pixel_pin = board.GP28
num_pixels = 28

skip_leds = int(num_pixels/4)
brink_leds = skip_leds-4

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False)
midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=(0,1,2,3))

while True:
    msg_in = midi.receive()
    if isinstance(msg_in, NoteOn) and msg_in.velocity != 0:
        vol=(msg_in.note-57)*3*3*3/7+25
        ch=msg_in.channel*skip_leds
        pixels[ch:ch+brink_leds]=(vol,vol,vol)
        pixels.show()
    if isinstance(msg_in, NoteOff):
        ch=msg_in.channel*skip_leds
        pixels[ch:ch+brink_leds]=(0,0,0)
        pixels.show()
