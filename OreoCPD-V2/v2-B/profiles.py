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
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 14

# stuff i defined for simplicity #
                                 #
def splash():					 #
    lcd.clear()					 #
    lcd.backlight_on()			 #
    lcd.move_to(3,0)			 #
    lcd.putstr("OreoCPD")		 #
    lcd.move_to(5,1)			 #
    lcd.putstr("v2-B")			 #
                                 #
def lcdprep():					 #
    lcd.backlight_on()			 #
    lcd.clear()					 #
    lcd.move_to(0,0)			 #
                                 #
def loading():					 #
    lcd.move_to(2,1)			 #
    lcd.putstr("Loading...")	 #
                                 #
def holup():					 #
    utime.sleep(.15)			 #
                                 #
def done():						 #
    lcd.move_to(2,1)			 #
    lcd.putstr("ready!")		 #
    print("profile loaded!")	 #
                                 #
def rst():						 #
    device.dev_0.off()			 #
    device.dev_1.off()			 #
    device.dev_2.off()			 #
    device.dev_3.off()			 #
    device.dev_4.off()			 #
    device.dev_5.off()			 #
    device.dev_6.off()			 #
    device.dev_7.off()			 #
    device.dev_8.off()			 #
    device.dev_9.off()			 #
##################################

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


# Profiles #

# Darkmode
def pro_0():
    lcdprep()
    lcd.putstr("Blackout:")
    loading()
    
    # Console message
    print("Darkmode loading...")
    
    # Functionality
    rst()
    holup()
    
    # Ready Message (black screen in this case)
    lcd.clear()
    lcd.backlight_off()
############################
    
# Basic
def pro_1():
    lcdprep()
    lcd.putstr("Basic:")
    loading()
    
    # Console Message
    print("Barebones AF")
    
    # Doin' things
    rst()
    device.dev_1.on()	# amp
    holup()

    # Print the ready message
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Econobox")
    done()
############################

# Essentials
def pro_2():
    lcdprep()
    lcd.putstr("Essentials:")
    loading()
    
    # Console Message
    print("Basic Driver")
    
    # Doin' Stuff
    rst()
    device.dev_1.on()  	# amp
    holup()
    device.dev_2.on()  	# acc
    holup()
    device.dev_3.on()  	# det
    holup()

    
    # Print the ready message
    lcd.clear()
    lcd.putstr("Essentials")
    done()
############################
    
def pro_3():
    lcdprep()
    lcd.putstr("Vibin'")
    loading()
    
    # Console Message
    print("focus")
    
    # Doing the things
    rst()
    device.dev_1.on()  	# amp
    holup()
    device.dev_2.on()  	# acc
    holup()
    device.dev_4.on()   # inv
    holup()
    
    # Print the ready message
    lcd.clear()
    lcd.putstr("Vibin'")
    done()
    
def pro_4():
    lcdprep()
    lcd.putstr("Boxin'")
    loading()
    
    # Console Message
    print("hottboxx")
    
    # Running the gauntlet
    rst()
    device.dev_1.on()  # amp
    holup()
    device.dev_2.on()  # acc
    holup()
    device.dev_3.on()  # det
    holup()
    device.dev_4.on()   # inv
    holup()
    
    # Print the ready message
    lcd.clear()
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
