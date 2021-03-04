#Prepared for dsPIC33CK256MP508_MCLV2.X demo
#Changes MCU output pin and validates
from threading import Timer
import time

#ASCII console color codes
RED = "\033[31m"
GREEN = "\033[32m"
DEFAULT = "\033[0m"

print "####################"
print "Led switch test"
print "####################"

#Get symbols by name
ledVariable = x2c_symbol.getSymbol("led1Control")
#At a real test use another variable that reads back the output
ledFeedback = x2c_symbol.getSymbol("led1Control")

#Set up some helper functions
def validateLedState(state):
    ledFeedback.updateValue() #read value from the HW
    if state == ledFeedback.getValue():
        print GREEN + "Pass" + DEFAULT
    else:
        print  RED + "Failed" + DEFAULT 

print "LED ON Test:"
ledVariable.setValue(True) #Thread to switch ON the LED
time.sleep(2) #Wait for switch
validateLedState(True) #validate new state

print "\nLED Off Test:"
ledVariable.setValue(False) #Switch OFF the LED
time.sleep(2) #Wait for switch
validateLedState(False) #validate new state
