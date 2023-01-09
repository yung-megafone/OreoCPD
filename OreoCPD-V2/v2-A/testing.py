#####################################
#         OreoCPD main.py           #
# Property DitoDevelopment LLC 2023 #
#####################################
from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi
from ir_rx import NEC_16
from machine import Pin
from machine import I2C
import profiles

# LCD stuff
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Main function that does all the doings
def main():
    # Initialize the LCD display
    i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    while input != 0 or if data > 0:  # NEC protocol sends repeat codes.
        # Clear display, enable backlight and reset pos to prevent issues
        lcd.clear()
        lcd.backlight_on()
        lcd.move_to(0,0)
            
        option = 0

        option = int(input("Please enter selection:  "))
        # Waiting for data and doing stuff when we recieve said data
        if data == 22 or input == 1:		# button 1 // Econobox
            profiles.pro_1()
        elif data == 25 or input == 2:	# button 2 // Daily
            profiles.pro_2()
        elif data == 13:	# button 3  // Dark
            profiles.pro_3()
        elif data == 12:	# button 4
            profiles.pro_4()
        elif data == 24:	# button 5
            profiles.pro_5()
        elif data == 94:	# button 6
            profiles.pro_6()
        elif data == 8:		# button 7
            profiles.pro_7()
        elif data == 28:	# button 8 
            profiles.pro_8()
        elif data == 90:	# button 9  // oh no popo
            profiles.pro_9()
        elif data == 82:	# button 0 // Default
            profiles.pro_0()
        else:
            print("Error, try again!")
                
# Run the program, dunno why its gotta be like this but micropython, amirite?
# Basically waits for a proper signal from the NEC protocol on pin 15 and calls function(main)
ir = NEC_16(Pin(15, Pin.IN), main)               