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
import programs as program
####################
description = "null" # set the progrssbar name to "null" as a placeholder

def clear_screen():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

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
            print("Default preset loading...\n")
            program.default()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("All devices ready!")
            print("##################")

        elif option == 2:
            clear_screen()
            print("Daily driver preset loading...\n")
            program.daily_driver()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("Essential devices ready!")
            print("########################")

        elif option == 3:
            clear_screen()
            print("Stealth preset loading...\n")
            program.dark_car()
            time.sleep(2) # sleep to ensure all relays are switched and devices are recieving power
            print("Everything but music is deactivated, be safe!")
            print("#############################################")
            ###     End the program    ###
        elif option == 9:
            print("Please make sure to disable the main power switch before parking for long periods of time!")
            time.sleep(2)
            print("\nGoodbye!")
            time.sleep(3)
            ###### Invalid input handler allows user to try another input #####

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
