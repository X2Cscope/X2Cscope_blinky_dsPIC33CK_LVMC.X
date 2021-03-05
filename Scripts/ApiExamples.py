import time
#ASCII console color codes
RED = "\033[31m"

print "####################"
print "Test Watchinterfaces - interacts directly with the watch view"
print "####################"
symbol = x2c_symbol.getSymbol("led1Control")
print "---"
print "Offset test"

try :
    print symbol.getOffset()
except:
    print RED + "No X2C watch instance found. Open X2C watch window and add led1Control first."
    sys.exit(1) #terminate

symbol.setOffset(symbol.getOffset()+1)
print symbol.getOffset()

print "---"
print "Scaling test"
print symbol.getScaling()
symbol.setScaling(symbol.getScaling()+1)
print symbol.getScaling()


print "---"
print "value tests"
symbol.getScaledValue()
symbol.setScaledValue(symbol.getScaledValue()+1)
print (symbol.getScaledValue()-symbol.getOffset())/symbol.getScaling()
print symbol.getValue()

print "---"
print "updateValue"
symbol.updateValue();
print symbol.getValue()
symbol.setValue(symbol.getValue()+1)
print symbol.getValue()



print "####################"
print "Test Scope interfaces - it uses its own instance, no sync with scope window"
print "####################"

x2c_scope.setChannelConfig(7, "myStruct.sinus", 1, 0)
x2c_scope.setTrigger(7, -0.7, "RISING", 0)
x2c_scope.setSampleTimeFactor(1)
x2c_scope.sample(False);


print x2c_scope.isSampleComplete()
time.sleep(3)
print x2c_scope.isSampleComplete()

x2c_scope.uploadData()

data = x2c_scope.getData()

for i in range(len(data)):
    print data[i]

