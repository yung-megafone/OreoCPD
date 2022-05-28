#############################################################################################
####    We want to define the modules as well as the functions to turn them on and off   ####
#############################################################################################
import time
from nntplib import GroupInfo
import RPi.GPIO as GPIO
                                ###########    DEVICES   ##########


# Use the bcm layout for gpio headers rather than board
## its just easier that way
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
## We are defining the output pins with names for cleanliness
### It's alot easier to know what 'sub_amp' controls rather than 12
#### Though with enough practice, anything is possible
sub_amp = 12
fwd_acc = 16
pwr_invt = 20
rad_det = 21
lig_mod = 6
com_scn = 13
sir_pa = 19
null_func = 26


# Prepare GPIO headers
## Basically telling the program that these pins are output pins
### Without it, the pi wouldnt know what to do with the outputs
#### i think...
GPIO.setup(sub_amp, GPIO.OUT)
GPIO.setup(fwd_acc, GPIO.OUT)
GPIO.setup(pwr_invt, GPIO.OUT)
GPIO.setup(rad_det, GPIO.OUT)
GPIO.setup(lig_mod, GPIO.OUT)
GPIO.setup(com_scn, GPIO.OUT)
GPIO.setup(sir_pa, GPIO.OUT)
GPIO.setup(null_func, GPIO.OUT)


# Sanitize the GIPO headers in case one is active for some reason...
## For example, a crash will cause whichever pins were 1 to remain active
### When restarting the program it will automatically set everything to 0. 
#### Clean slate sorta thing
GPIO.output(sub_amp, GPIO.LOW)
GPIO.output(fwd_acc, GPIO.LOW)
GPIO.output(pwr_invt, GPIO.LOW)
GPIO.output(rad_det, GPIO.LOW)
GPIO.output(lig_mod, GPIO.LOW)
GPIO.output(com_scn, GPIO.LOW)
GPIO.output(sir_pa, GPIO.LOW)
GPIO.output(null_func, GPIO.LOW)


                        ##############  toggle.  ###############

                                ########## Activate and Deavtivate the Devices ##########
                        ############## Turn devices Off ################
class toggle:
    ###  Civvie Stuff  ###
    def sub_on():   # Define a function
        GPIO.output(sub_amp, GPIO.HIGH)     # Set the output for "function" to 1
        print("Amplifier [Active] \n")     # Print to the console that the device has power
        time.sleep(1)       # sleep for a second so we don't overload the power supply
                            ## After all, the whole point of OreoCPD is to not blow fuses and melt stuff


    def acc_on():
        GPIO.output(fwd_acc, GPIO.HIGH)
        print("Accecories [Active] \n")
        time.sleep(1)


    def inv_on():
        GPIO.output(pwr_invt, GPIO.HIGH)
        print("Inverter [Active] \n")
        time.sleep(1)


    def rad_on():
        GPIO.output(rad_det, GPIO.HIGH)
        print("Radar [Active] \n")
        time.sleep(1)

        ###  Poop Stuff ###


    def lig_on():
        GPIO.output(lig_mod, GPIO.HIGH)
        print("Lighting [Active] \n")
        time.sleep(1)


    def com_on():
        GPIO.output(com_scn, GPIO.HIGH)
        print("Comms [Active] \n")
        time.sleep(1)


    def sir_on():
        GPIO.output(sir_pa, GPIO.HIGH)
        print("Sirens [Active] \n")
        time.sleep(1)


    def nul_on():
        GPIO.output(null_func, GPIO.HIGH)
        print("Null_ [Active] \n")
        time.sleep(1)


                            ############## Turn Devices Off ################

        ### Civvie Stuff ###


    def sub_off():
        GPIO.output(sub_amp, GPIO.LOW)
        print("Amplifier [Inactive] \n")
        time.sleep(1)


    def acc_off():
        GPIO.output(fwd_acc, GPIO.LOW)
        print("Accessories [Inactive] \n")
        time.sleep(1)


    def inv_off():
        GPIO.output(pwr_invt, GPIO.LOW)
        print("Inverter [Inactive] \n")
        time.sleep(1)


    def rad_off():
        GPIO.output(rad_det, GPIO.LOW)
        print("Radar [Inactive] \n")
        time.sleep(1)

        ###  Poop Stuff  ###


    def lig_off():
        GPIO.output(lig_mod, GPIO.LOW)
        print("Lighting [Inactive] \n")
        time.sleep(1)


    def com_off():
        GPIO.output(com_scn, GPIO.LOW)
        print("Comms [Inactive] \n")
        time.sleep(1)


    def sir_off():
        GPIO.output(sir_pa, GPIO.LOW)
        print("Sirens [Inactive] \n")
        time.sleep(1)


    def nul_off():
        GPIO.output(null_func, GPIO.LOW)
        print("Null_ [Inactive] \n")
        time.sleep(1)
