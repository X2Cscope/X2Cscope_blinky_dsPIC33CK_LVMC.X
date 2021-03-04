#Prepared for X2Cscope_blinky demo
#Changes MCU output pin
import time

print "####################"
print "Led switching test"
print "####################"

#Get symbols by name
ledVariable = x2c_symbol.getSymbol("led1Control")

for x in range(0, 3):

    print "LED ON"
    ledVariable.setValue(True) #Thread to switch ON the LED
    time.sleep(0.5) #Wait a bit

    print "LED OFF"
    ledVariable.setValue(False) #Switch OFF the LED
    time.sleep(0.5) #Wait a bit
