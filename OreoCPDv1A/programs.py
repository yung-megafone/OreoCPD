####################################################################################
###   Here we will define profiles and enable / disable the modules accordingy   ###
####################################################################################
from devices import toggle
import time

###############     Programs        #############

#   Startup loop enables all devices by default... If no means to control the system are avalible, everything stays on, it's amazing!
def default():
    profile = "Default"
    print("Default Profile Selected \n")
    toggle.sub_on()
    toggle.acc_on()
    toggle.inv_on()
    toggle.rad_on()
    toggle.lig_on()
    toggle.com_on()
    toggle.sir_on()
    toggle.nul_on()
    time.sleep(1)
    print("Default Profile Loaded \n")


#   Dark Car Preset allows Subwoofer to be active while not allowing power to light emiting devices
def dark_car():
    profile = "Dark Car"
    print("Dark Car Profile Selected \n")
    toggle.sub_on()
    toggle.acc_off()
    toggle.inv_off()
    toggle.rad_off()
    toggle.lig_off()
    toggle.com_off()
    toggle.sir_off()
    toggle.nul_off()
    time.sleep(1)
    print('Dark Car Profile Loaded \n')


#  Daily Driver preset enables subs, accessory poerts, and radar detector
def daily_driver():
    profile = "Daily"
    print("Daily Driver Profile Selected \n")
    toggle.sub_on()
    toggle.acc_on()
    toggle.inv_on()
    toggle.rad_on()
    toggle.lig_off()
    toggle.com_on()
    toggle.sir_off()
    toggle.nul_off()
    time.sleep(1)
    print("Daily Driver Profile Loaded \n")


def demo():
    ## Show some cool stuff this app can do ##
    profile = "Demo"
    print("Demo Profile Selected \n")
    toggle.sub_on()
    time.sleep(1)
    toggle.sub_off()
    toggle.acc_on()
    time.sleep(1)
    toggle.acc_off()
    toggle.inv_on()
    time.sleep(1)
    toggle.inv_off()
    toggle.rad_on()
    time.sleep(1)
    toggle.rad_off()
    toggle.lig_on()
    time.sleep(1)
    toggle.lig_off()
    toggle.com_on()
    time.sleep(1)
    toggle.com_off()
    toggle.sir_on()
    time.sleep(1)
    toggle.sir_off()
    toggle.nul_on()
    time.sleep(1)
    toggle.nul_off()
    time.sleep(1)
    print("Demo Profile Loaded \n")

    

def all_off():
    profile = "Shutdown"
    print("Shutting everything down...\n")
    toggle.sub_off()
    toggle.acc_off()
    toggle.inv_off()
    toggle.rad_off()
    toggle.lig_off()
    toggle.com_off()
    toggle.sir_off()
    toggle.nul_off()
    time.sleep(1)
    print("All devices are disabled...")
