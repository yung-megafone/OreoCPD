# Oreo CPD 20220420
# v1.0 20220424
# Property REDLINE TECHNOLOGY LLC 2022




                                    ##########   Setup   ##########
                            ############     General Setup     ############
import time
from turtle import clear
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
    ### Providing an alternate loopback point to not reset modules on bad input ###

profile = ""

def main():
    clear_screen()
    option = 0 # set the input variable 'option' to 0
        ### Loop thru the menu items and when one is selected, execute the underlying commands. Otherwise restart the program with an error message
    while option is not 1:
        print("Menu\n")
        print(" [1] Quit\n\n [2] Demo\n\n [3] Default\n\n [4] Daily\n\n [5] Stealth\n\n [6] Disable\n\n" )
        print(f'The currently selected profile is {profile}')
        print("")
        option = int(input("Please enter selection:  "))

        if option == 2: # demo #
            clear_screen()
            program.demo()
            # sleep to ensure all relays are switched and devices are recieving power before continuing
            time.sleep(2)


        elif option == 3:   # defualt #
            clear_screen()
            program.default()
            time.sleep(2)


        elif option == 4:   # daily #
            clear_screen()
            program.daily_driver()
            time.sleep(2)


        elif option == 5:   # stealth #
            clear_screen()
            program.dark_car()
            time.sleep(2)


        elif option == 6:   # poweroff #
            clear_screen()
            program.all_off()
            time.sleep(2)

        
        elif option == 7:   # popo #
            clear_screen()
            program.popo()
            time.sleep(2)


            ###     End the program    ###
        elif option == 1:
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
    program.default() # load the default profile
    time.sleep(1)
    main()

oreocpd()


GPIO.cleanup()
