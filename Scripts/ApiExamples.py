import time
print "!Limitation! Struct members must be listed in the X2C Watch view"
print "####################"
print "Test Watchinterfaces"
print "####################"
symbol = x2c_symbol.getSymbol("myStruct.ledOn")
print "---"
print "Offset test"
print symbol.getOffset()
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
print "Test Scope interfaces"
print "####################"

x2c_scope.setChannelConfig(7, "sinus", 1, 0)
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

