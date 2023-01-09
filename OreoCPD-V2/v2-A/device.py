#####################################
#        OreoCPD device.py          #
# Property DitoDevelopment LLC 2023 #
#####################################
from machine import Pin
import machine

# Pinout // device connections
dev_0 = Pin(00, Pin.OUT)	# Save
dev_1 = Pin(6, Pin.OUT)	    # AMP
dev_2 = Pin(7, Pin.OUT)	    # ACC
dev_3 = Pin(8, Pin.OUT)	    # DET
dev_4 = Pin(9, Pin.OUT)	    # INV
dev_5 = Pin(10, Pin.OUT)	# NULL
dev_6 = Pin(11, Pin.OUT)	# NULL
dev_7 = Pin(12, Pin.OUT)	# NULL
dev_8 = Pin(13, Pin.OUT)	# NULL

# Device functions
def dev_0_off():
    dev_0(0)    
def dev_0_on():
    dev_0(1)
    
def dev_1_off():
    dev_1(0)    
def dev_1_on():
    dev_1(1)
    
def dev_2_off():
    dev_2(0)    
def dev_2_on():
    dev_2(1)
    
def dev_3_off():
    dev_3(0)    
def dev_3_on():
    dev_3(1)
    
def dev_4_off():
    dev_4(0)    
def dev_4_on():
    dev_4(1)
    
def dev_5_off():
    dev_5(0)    
def dev_5_on():
    dev_5(1)
    
def dev_6_off():
    dev_6(0)    
def dev_6_on():
    dev_6(1)
    
def dev_7_off():
    dev_7(0)    
def dev_7_on():
    dev_7(1)
    
def dev_8_off():
    dev_8(0)    
def dev_8_on():
    dev_8(1)
    
def dev_9_off():
    dev_9(0)    
def dev_9_on():
    dev_9(1)