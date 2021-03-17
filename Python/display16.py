#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
from time import sleep
from random import randint

# this example uses a single shift register with normal 2-pin LED's

'''
SER   = Data
RCLK  = Latch
SRCLK = Clock
SRCLR = Clear (keep high)
OE    = Blank (keep low)

       74HC595
       -------
 QB --|1    16|-- VCC
 QC --|2    15|-- QA
 QD --|3    14|-- SER
 QE --|4    13|-- OE
 QF --|5    12|-- RCLK
 QG --|6    11|-- SRCLK
 QH --|7    10|-- SRCLR
GND --|8     9|-- QH'           <--- DATA OUT to SER on next IC to daisy chain them
       -------
'''

data_pin  = "P8_8"
latch_pin = "P8_10"
clock_pin = "P8_12"
clear_pin = "P8_14"
blank_pin = "P8_16"

# Setup Pins
GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(clear_pin, GPIO.OUT)
GPIO.setup(blank_pin, GPIO.OUT)

# Set Pin State
GPIO.output(data_pin, GPIO.LOW)
GPIO.output(latch_pin, GPIO.LOW)
GPIO.output(clock_pin, GPIO.LOW)
#GPIO.output(clear_pin, GPIO.LOW)
GPIO.output(clear_pin, GPIO.HIGH)
GPIO.output(blank_pin, GPIO.LOW)


def delay(millis):
    millis_to_seconds = float(millis)/1000
    return sleep(millis_to_seconds)
    
char = {
     '0': '1111111100100010',
     '1': '0000010000001100',
     '2': '1000100001110111',
     '3': '0000100000111111',
     '4': '0011000111000000',
     '5': '1001000010110011',
     '6': '1000100011111011',
     '7': '0000000000001111',
     '8': '1000100011111111',
     '9': '1000100010111111',
     'A': '1000100011001111',
     'B': '0010101000111111',
     'C': '0000000011110011',
     'D': '0010001000111111',
     'E': '1000000011110011',
     'F': '1000000011000011',
     'G': '0000100011111011',
     'H': '1000100011001100',
     'I': '0010001000110011',
     'J': '0000000001111100',
     'K': '1001010011000000',
     'L': '0000000011110000',
     'M': '0000010111001100',
     'N': '0001000111001100',
     'O': '0000000011111111',
     'P': '1000100011000111',
     'Q': '0001000011111111',
     'R': '1001100011000111',
     'S': '1000100010111011',
     'T': '0010001000000011',
     'U': '0000000011111100',
     'V': '0100010011000000',
     'W': '0101000011001100',
     'X': '0101010100000000',
     'Y': '1000100010111100',
     'Z': '0100010000110011',
     'a': '1010000001110000',
     'b': '1010000011100000',
     'c': '1000000001100000',
     'd': '0010100000011100',
     'e': '1100000001100000',
     'f': '1010101000000010',
     'g': '1010001010100001',
     'h': '1010000011000000',
     'i': '0010000000000000',
     'j': '0010001001100000',
     'k': '0011011000000000',
     'l': '0000000011000000',
     'm': '1010100001001000',
     'n': '1010000001000000',
     'o': '1010000001100000',
     'p': '1000001011000001',
     'q': '1010001010000001',
     'r': '1000000001000000',
     's': '1010000010100001',
     't': '1000000011100000',
     'u': '0010000001100000',
     'v': '0100000001000000',
     'w': '0101000001001000',
     'x': '0101010100000000',
     'y': '0000101000011100',
     'z': '1100000000100000',
     ' ': '0000000000000000',
     '!': '0000000000001100',
     '"': '0000001000000100',
     '#': '1010101000111100',
     '$': '1010101010111011',
     '%': '1110111010011001',
     '&': '1001001101110001',
     '\'': '0000001000000000',
     '(': '0001010000000000',
     ')': '0100000100000000',
     '*': '1111111100000000',
     '+': '1010101000000000',
     ',': '0100000000000000',
     '-': '1000100000000000',
     '.': '0001000000000000',
     '/': '0100010000000000',
     ':': '0010001000000000',
     ';': '0100001000000000',
     '<': '1001010000000000',
     '=': '1000100000110000',
     '>': '0100100100000000',
     '?': '0010100000000111',
     '@': '0000101011110111',
     '[': '0010001000010010',
     '\\': '0001000100000000',
     ']': '0010001000100001',
     '^': '0101000000000000',
     '_': '0000000000110000',
     '`': '0000000100000000',
     '{': '1010001000010010',
     '|': '0010001000000000',
     '}': '0010101000100001',
     '~': '1100110000000000'
}



output = char['1']
print (output)
GPIO.output(clear_pin, GPIO.LOW)
GPIO.output(clear_pin, GPIO.HIGH)
GPIO.output(latch_pin, GPIO.HIGH)
GPIO.output(latch_pin, GPIO.LOW)
for c in output:
   print(c)
   if c == '1':
      GPIO.output(data_pin, GPIO.HIGH)
      GPIO.output(clock_pin, GPIO.HIGH)
      GPIO.output(clock_pin, GPIO.LOW)
      GPIO.output(data_pin, GPIO.LOW)
   if c == '0':
      GPIO.output(clock_pin, GPIO.HIGH)
      GPIO.output(clock_pin, GPIO.LOW)

GPIO.output(latch_pin, GPIO.HIGH)
GPIO.output(latch_pin, GPIO.LOW)


