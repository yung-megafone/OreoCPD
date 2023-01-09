#####################################
#       OreoCPD profiles.py         #
# Property DitoDevelopment LLC 2023 #
#####################################
from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi
from machine import I2C
import machine
import device
import utime

# LCD stuff
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# stuff i defined for simplicity #
                                 #
def loading():					 #
    lcd.move_to(1,1)			 #
    lcd.putstr("Loading...")	 #
                                 #
def holup():					 #
    utime.sleep(.15)			 #
                                 #
def done():						 #
    lcd.move_to(1,2)			 #
    lcd.putstr("ready!")		 #
    print("profile loaded!")	 #
##################################

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# Profiles #

# Darkmode
def pro_0():
    lcd.clear()
    lcd.putstr("Blackout:")
    loading()
    
    # Console message
    print("Darkmode loading...")
    
    # Functionality
    device.dev_0.off()
    holup()
    device.dev_1.off()
    holup()
    device.dev_2.off()
    holup()
    device.dev_3.off()
    holup()
    device.dev_4.off()
    holup()
    device.dev_5.off()
    holup()
    device.dev_6.off()
    holup()
    device.dev_7.off()
    holup()
    device.dev_8.off()
    holup()
    device.dev_9.off()
    lcd.backlight_off()
############################
    
# Basic
def pro_1():
    lcd.clear()
    lcd.putstr("Basic:")
    loading()
    
    # Console Message
    print("Barebones AF")
    
    # Doin' things
    device.dev_0.off()
    holup()
    device.dev_1.on()	# amp
    holup()
    device.dev_2.off()
    holup()
    device.dev_3.off()
    holup()
    device.dev_4.off()
    holup()
    device.dev_5.off()
    holup()
    device.dev_6.off()
    holup()
    device.dev_7.off()
    holup()
    device.dev_8.off()
    holup()
    device.dev_9.off()
    
    # Print the ready message
    lcd.clear()
    lcd.putstr("Econobox")
    done()
############################

# Essentials
def pro_2():
    lcd.clear()
    lcd.putstr("Essentials:")
    loading()
    
    # Console Message
    print("Basic Driver")
    
    # Doin' Stuff
    device.dev_0.off()	# save
    holup()
    device.dev_1.on()  	# amp
    holup()
    device.dev_2.on()  	# acc
    holup()
    device.dev_3.on()  	# det
    holup()
    device.dev_4.off()
    holup()
    device.dev_5.off()
    holup()
    device.dev_6.off()
    holup()
    device.dev_7.off()
    holup()
    device.dev_8.off()
    holup()
    device.dev_9.off()
    holup()
    
    # Print the ready message
    lcd.clear()
    lcd.putstr("Essentials")
    done()
############################
    
def pro_3():
    lcd.clear()
    lcd.putstr("Vibin'")
    loading()
    
    # Console Message
    print("focus")
    
    # Doing the things
    device.dev_0.off()	# save
    holup()
    device.dev_1.on()  	# amp
    holup()
    device.dev_2.on()  	# acc
    holup()
    device.dev_3.off()  # det
    holup()
    device.dev_4.on()   # inv
    holup()
    device.dev_5.off()
    holup()
    device.dev_6.off()
    holup()
    device.dev_7.off()
    holup()
    device.dev_8.off()
    holup()
    device.dev_9.off()
    holup()
    
    # Print the ready message
    lcd.clear()
    lcd.putstr("Vibin'")
    done()
    
def pro_4():
    lcd.clear()
    lcd.putstr("Boxin'")
    loading()
    
    # Console Message
    print("hottboxx")
    
    # Running the gauntlet
    device.dev_0.off()
    holup()
    device.dev_1.on()  # amp
    holup()
    device.dev_2.on()  # acc
    holup()
    device.dev_3.on()  # det
    holup()
    device.dev_4.on()   # inv
    holup()
    device.dev_5.off()
    holup()
    device.dev_6.off()
    holup()
    device.dev_7.off()
    holup()
    device.dev_8.off()
    holup()
    device.dev_9.off()
    holup()
    
    lcd.putstr("Boxin'")
    done()
############################

# Other profiles for future expansion
def pro_5():
    lcd.clear()
    lcd.putstr("Profile 5")
    print("Profile 5")

    
def pro_6():
    lcd.clear()
    lcd.putstr("Profile 6")
    print("Profile 6")

    
def pro_7():
    lcd.clear()
    lcd.putstr("Profile 7")
    print("Profile 7")

    
def pro_8():
    lcd.clear()
    lcd.putstr("Profile 8")
    print("Profile 8")

    
def pro_9():
    lcd.clear()
    lcd.putstr("Profile 9")
