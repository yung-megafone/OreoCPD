# Oreo CPD 20220420
# v1.0 20220424
# Property REDLINE TECHNOLOGY LLC 2022




                                    ##########   Setup   ##########
                            ############     General Setup     ############
import time
import RPi.GPIO as GPIO
from tqdm import tqdm , trange
from tqdm.notebook import tqdm_notebook
import os

####################
description = "null" # set the progrssbar name to"null" as a placeholder

def clear_screen():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

                                ###########    GPIO SETUP   ##########
# Use the bcm layout for gpio headers rather than board
GPIO.setmode(GPIO.BCM) 

# Define GPIO pins
sub_amp=12
fwd_acc=16
pwr_invt=20
rad_det=21
lig_mod=6
com_scn=13
sir_pa=19
null_func=26


# Prepare GPIO headers
GPIO.setup(sub_amp, GPIO.OUT)
GPIO.setup(fwd_acc, GPIO.OUT)
GPIO.setup(pwr_invt, GPIO.OUT)
GPIO.setup(rad_det, GPIO.OUT)
GPIO.setup(lig_mod, GPIO.OUT)
GPIO.setup(com_scn, GPIO.OUT)
GPIO.setup(sir_pa, GPIO.OUT)
GPIO.setup(null_func, GPIO.OUT)

# Set all pins to low, mostly for program resets and such
GPIO.output(sub_amp, GPIO.LOW)
GPIO.output(fwd_acc, GPIO.LOW)
GPIO.output(pwr_invt, GPIO.LOW)
GPIO.output(rad_det, GPIO.LOW)
GPIO.output(lig_mod, GPIO.LOW)
GPIO.output(com_scn, GPIO.LOW)
GPIO.output(sir_pa, GPIO.LOW)
GPIO.output(null_func, GPIO.LOW)

                            ##########   Activate and Deavtivate Modules     ###########

# Turn Modules On
    ###     Citizen Stuff   ###
def sub_on():
    GPIO.output(sub_amp, GPIO.HIGH)
    print("Amplifier [Active]")
    print("")
    time.sleep(1)

def acc_on():
    GPIO.output(fwd_acc, GPIO.HIGH)
    print("Accecories [Active]")
    print("")
    time.sleep(1)

def inv_on():
    GPIO.output(pwr_invt, GPIO.HIGH)
    print("Inverter [Active]")
    print("")
    time.sleep(1)

def rad_on():
    GPIO.output(rad_det, GPIO.HIGH)
    print("Radar [Active]")
    print("")
    time.sleep(1)

    ###    Polide Equiptment    ###
def lig_on():
    GPIO.output(lig_mod, GPIO.HIGH)
    print("Lighting [Active]")
    print("")
    time.sleep(1)

def com_on():
    GPIO.output(com_scn, GPIO.HIGH)
    print("Comms [Active]")
    print("")
    time.sleep(1)

def sir_on():
    GPIO.output(sir_pa, GPIO.HIGH)
    print("Sirens [Active]")
    print("")
    time.sleep(1)

def nul_on():
    GPIO.output(null_func, GPIO.HIGH)
    print("Null_ [Active]")
    print("")
    time.sleep(1)

# Turn Modules Off
    ### Civvie Stuff ###
def sub_off():
    GPIO.output(sub_amp, GPIO.LOW)
    print("Amplifier [Inactive]")
    print("")
    time.sleep(1)

def acc_off():
    GPIO.output(fwd_acc, GPIO.LOW)
    print("Accessories [Inactive]")
    print("")
    time.sleep(1)


def inv_off():
    GPIO.output(pwr_invt, GPIO.LOW)
    print("Inverter [Inactive]")
    print("")
    time.sleep(1)

def rad_off():
    GPIO.output(rad_det, GPIO.LOW)
    print("Radar [Inactive]")
    print("")
    time.sleep(1)

    ###     Police Equiptment  ###
def lig_off():
    GPIO.output(lig_mod, GPIO.LOW)
    print("Lighting [Inactive]")
    print("")
    time.sleep(1)

def com_off():
    GPIO.output(com_scn, GPIO.LOW)
    print("Comms [Inactive]")
    print("")
    time.sleep(1)

def sir_off():
    GPIO.output(sir_pa, GPIO.LOW)
    print("Sirens [Inactive]")
    print("")
    time.sleep(1)

def nul_off():
    GPIO.output(null_func, GPIO.LOW)
    print("Null_ [Inactive]")
    print("")
    time.sleep(1)


                                ###############     Programs        #############

#   Startup loop enables all devices by default... If no means to control the system are avalible, everything stays on, it's amazing!
def default():
    print("Default Preset Selected")
    print("")
    sub_on()
    acc_on()
    inv_on()
    rad_on()
    lig_on()
    com_on()
    sir_on()
    nul_on()

#   Dark Car Preset allows Subwoofer to be active while not allowing power to in-cab light emiting devices
def dark_car():
    print("Dark Car Preset Selected")
    print("")
    sub_on()
    acc_off()
    inv_off()
    rad_off()
    lig_off()
    com_off()
    sir_off()
    nul_off()

#  Daily Driver preset enables subs, accessory poerts, and radar detector
def daily_driver():
    print("Daily Driver Preset Selected")
    print("")
    sub_on()
    acc_on()
    inv_on()
    rad_on()
    lig_off()
    com_on()
    sir_off()
    nul_off()
    


##################################################################

###     Menu and Program     ###
    ###Providing an alternate loopback point to not reset modules on bad input ###
def main():
    clear_screen()
    option = 0 # set the input variable 'option' to 0
        ### Loop thru the menu items and when one is selected, execute the underlying commands. Otherwise restart the program with an error message
    while option < 9:
        print("[1] Default\n\n [2] Daily\n\n [3] Dark Car\n")
        print("")
        option = int(input("Please enter selection:  "))

        if option == 1:
            clear_screen()
            print("Default preset loading...")
            print("")
            default()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("All devices ready!")
            print("##################")

        elif option == 2:
            clear_screen()
            print("Daily driver preset loading...")
            print("")
            daily_driver()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("Essential devices ready!")
            print("########################")

        elif option == 3:
            clear_screen()
            print("Stealth preset loading...")
            print("")
            dark_car()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("Everything but music is deactivated, be safe!")
            print("#############################################")
            ###     End the program    ###
        elif option == 9:
            print("Please make sure to disable the main power switch before parking for long periods of time!")
            time.sleep(2)
            print("")
            print("Goodbye!")
            time.sleep(3)
            ###### Invalid input handler allows user to try another input #####
        else:
            print("input invalid!")
            print("##############")
            main()    

def oreocpd():
    print("System Starting()")
    print("")
    default() # load the default profile
    time.sleep(1)
    main()

oreocpd()


GPIO.cleanup()
