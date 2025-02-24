# Copyright (C) 2025 Edward J. Gonell Rodríguez (@EdwardGonell)
# This file is part of GR8-1-Homebrew-CPU.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3. See LICENSE-GPL-3.0.txt.

"""Instruction Register Controls for the Control Unit Programmer."""

from machine import Pin
from time import sleep

# Define pins for 74HC595 shift register and 74163 counter
ser = Pin(29, Pin.OUT)    # Serial data input (74HC595 DS)
i_oe = Pin(28, Pin.OUT)   # Instruction output enable (active low, unused here)
rclk = Pin(27, Pin.OUT)   # Register clock (74HC595 RCLK)
sclk = Pin(26, Pin.OUT)   # Shift clock (74HC595 SRCLK)
clr = Pin(19, Pin.OUT)    # Clear (active low, 74HC595 SRCLR)
ldi = Pin(18, Pin.OUT)    # Load instruction (active low)
ii = Pin(17, Pin.OUT)     # Increment instruction (74163 clock)
clk = Pin(16, Pin.OUT)    # Main clock for counter
we = Pin(2, Pin.OUT)      # EEPROM write enable (active low)

clr.high()    # Disable clear
we.high()     # Disable EEPROM write

clk_time = 0.000001    # 1µs clock pulse (adjust based on hardware)

def tick():                # Clock pulse for counter
    clk.high()
    sleep(clk_time)
    clk.low()
    sleep(clk_time)

def s_tick():              # Shift clock pulse for 74HC595
    sclk.high()
    sleep(clk_time)
    sclk.low()
    sleep(clk_time)

def r_tick():              # Latch data to 74HC595 outputs
    rclk.high()
    sleep(clk_time)
    rclk.low()
    sleep(clk_time)

def clear():               # Reset shift register
    clr.low()
    tick()
    clr.high()
    tick()

def send(data):            # Send 8-bit data to shift register
    clr.low()
    sleep(clk_time)
    clr.high()
    
    for i in range(8):
        ser.value(data >> i & 1)    # Shift out LSB first
        s_tick()
    r_tick()                        # Latch to outputs

def load_instruction():     # Load shift register data (e.g., into counter)
    ldi.low()
    tick()
    ldi.high()

def instruction_increment():    # Increment 74163 counter
    ii.high()
    tick()
    ii.low()

def instruction(value):    # Set an 8-bit instruction value
    send(value)
    load_instruction()
