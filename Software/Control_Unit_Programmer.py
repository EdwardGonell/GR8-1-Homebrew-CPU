# Copyright (C) 2025 Edward J. Gonell Rodríguez (@EdwardGonell)
# This file is part of GR8-1-Homebrew-CPU.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3. See LICENSE-GPL-3.0.txt.

from machine import Pin
from time import sleep, sleep_ms
from Control_Unit import Instruction_Upload, Programmer_Serial

eeprom_write_enable = Pin(2, Pin.OUT)
address_12 = Pin(0, Pin.OUT)
eeprom_write_enable.high()

Serial    =    Programmer_Serial
Instruction_Upload.clear()


def write_tick():							# A clock cycle for the write enable pin
    eeprom_write_enable.low()
    sleep_ms(10)							# 10ms low pulse for EEPROM write
    eeprom_write_enable.high()
    sleep_ms(10)							# 10ms high for the data to latch
            
def set_address(address_13_bit):			# Sets a 13 bit address
    Instruction_Upload.clear()				# Clears the instruction register     
    if address_13_bit >= 0x1000:			# A12 high for adresses >= 0x1000
        address_12.high()
    elif address_13_bit  < 0x1000:			# A12 low for adresses <= 0x1000
        address_12.low()
    
    middle = (address_13_bit & 0x0FF0) >> 4	# Bits A4-A11
    Instruction_Upload.instruction(middle)
    
    bottom = (address_13_bit & 0x000F)		# Bits A0-A3
    for i in range(bottom):					# Count up 74163 for bottom 4 bits
        Instruction_Upload.instruction_increment()
        
def write(address_13_bit, control_lines):	# Sends 24 bits of data to a certain address
    Instruction_Upload.clr.low()
    sleep(0.000001)							# 1us clear pulse
    Instruction_Upload.clr.high()
    set_address(address_13_bit)				# Sets the desired address
    Serial.write(control_lines)				# Writes a 24 bit value to the EEPROM
    write_tick()
    
def fill(value_24_bit):						# Fills the eeprom with a certain value
    Serial.write(value_24_bit)
    for i in range(2**13):
        set_address(i)
        write_tick()

def comb(frequency):						# Will comb through all the addresses at a certain frequency
    set_address(0)
    for i in range(2**13):
        set_address(i)
        sleep(1/frequency)
        
def write_protection_disable():				# Write protection disable for the X28HC64P-12
    set_address(0x1555)
    Instruction_Upload.instruction(0xAAAAAA)
    write_tick()
    set_address(0x0AAA)
    Instruction_Upload.instruction(0x555555)
    write_tick()
    set_address(0x1555)
    Instruction_Upload.instruction(0x808080)
    write_tick()
    set_address(0x1555)
    Instruction_Upload.instruction(0xAAAAAA)
    write_tick()
    set_address(0x0AAA)  
    Instruction_Upload.instruction(0x555555)
    write_tick()
    set_address(0x1555)
    Instruction_Upload.instruction(0x202020)
    write_tick()
