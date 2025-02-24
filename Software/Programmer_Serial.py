# Copyright (C) 2025 Edward J. Gonell Rodríguez (@EdwardGonell)
# This file is part of GR8-1-Homebrew-CPU.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3. See LICENSE-GPL-3.0.txt.

"""Control Line Shift Register for the Control Unit Programmer."""

from machine import Pin
from time import sleep


ser = Pin(7, Pin.OUT)
sclk = Pin(6, Pin.OUT)  
rclk = Pin(5, Pin.OUT)
clr = Pin(4, Pin.OUT)
frequency = 1000
def s_tick():
    sclk.high()
    sleep(1/frequency)
    sclk.low()
    sleep(1/frequency)
    
def r_tick():
    rclk.high()
    sleep(1/frequency)
    rclk.low()
    sleep(1/frequency)

def sr_tick():
    sclk.high()
    rclk.low()
    sleep(1/frequency)
    sclk.low()
    rclk.high()
    sleep(1/frequency)
    
def write(data): 
    clr.low()
    sleep(1/frequency)
    clr.high()

    if isinstance(data, int):
        # If data is an integer, convert it to bits
        bits = [(data >> i) & 1 for i in range(24)]
    else:
        bits = data

    for i in range(24):
        # Set the data bit
        ser.value(bits[i] if isinstance(bits[i], bool) else bool(bits[i]))
        s_tick()
    r_tick()
        

    


